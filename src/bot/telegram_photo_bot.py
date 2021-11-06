import logging
from pathlib import Path
from telegram import Update
from telegram.ext import CallbackContext
from bot.date_utils import DateUtil


class PhotoBot:
    def __init__(self, root_dir) -> None:
        self._logger = logging.getLogger(__name__)
        self._root_dir = root_dir
        self._max_cache_time_in_sec = 120
        self._cached_dir_info = {}
        if not Path(self._root_dir).is_dir():
            raise RootFolderDoesNotExistException

    def receiveUpdate(self, update: Update, context: CallbackContext) -> None:

        self._logger.info(update)

        if not self._isPostForBot(update):
            return

        update_file_name = self._getFileNameFromMessage(update.message)
        update_file_id = self._getFileIdFromMessage(update.message)

        path = self._getCachedDirectoryNameForPost(update.message)

        if path:
            self._downloadFileForPath(update.message, context, update_file_id, update_file_name, path)
            return

        update_comment = self._getCommentFromUpdateMessage(update.message)

        path = self._createDirectoryNameForPost(update.message, update_file_name, update_comment)

        if path:
            self._setCachedDirectoryNameForPost(path, update.message)
            self._downloadFileForPath(update.message, context, update_file_id, update_file_name, path)

    def _createFullLocalName(self, path, update_file_name):
        full_local_name = path + "/" + update_file_name
        return full_local_name

    def _createDirectoryNameForPost(self, message, update_file_name: str, update_comment: str):

        post_dir = None
        if DateUtil.isStartWithDate(update_comment):
            post_dir = update_comment

        if not post_dir and DateUtil.isContainRawDate(update_file_name):
            post_dir = DateUtil.makeDateString(update_file_name) + " " + update_comment

        if not post_dir:
            message.reply_text("Не смог найти дату события")
            raise DateNotFoundException('Date not found in post data')

        full_path = self._root_dir + "/" + post_dir
        return full_path

    def _getCommentFromUpdateMessage(self, message):
        if not message.caption or not message.caption.strip():
            message.reply_text("Нужно указать название для поста")
            raise CommentIsEmptyException()
        return message.caption.strip()

    def _getFileNameFromMessage(self, message):
        update_file_name = None
        if message.document:
            update_file_name = message.document.file_name
        if not update_file_name:
            message.reply_text("Нет файлов в посте")
            raise FileNameNotFoundException
        return update_file_name

    def _getFileIdFromMessage(self, message):
        update_file_id = None
        if message.document:
            update_file_id = message.document.file_id
        if not update_file_id:
            message.reply_text("Нет файлов в посте")
            raise FileIdNotFoundException
        return update_file_id

    def _getCachedDirectoryNameForPost(self, message):
        path = None
        if message.date and self._cached_dir_info:
            if message.date.timestamp() - self._cached_dir_info['date'].timestamp() <= self._max_cache_time_in_sec:
                path = self._cached_dir_info['dir']
            else:
                self._cached_dir_info = None
        return path

    def _setCachedDirectoryNameForPost(self, path, message):
        if message.date:
            self._cached_dir_info = {'dir': path, 'date': message.date}

    def _downloadFileForPath(self, message, context, update_file_id, update_file_name, path):
        if not Path(path).is_dir():
            Path(path).mkdir()
        try:
            self.downloadFile(context, update_file_id, self._createFullLocalName(path, update_file_name))
        except Exception as exc:
            message.reply_text("Не смог сохранить файл")
            raise exc

    def downloadFile(self, context, update_file_id, full_local_name):
        context.bot.getFile(update_file_id).download(full_local_name)

    def _isPostForBot(self, update):
        if update.message.chat.type == 'private':
            return True
        if update.message.chat.type == 'group' and self.isBotMentionedInPost(update):
            return True
        return False

    def isBotMentionedInPost(self, update):
        mentioned = [e for e in update.message.entities if e.type == 'mention']
        return len(mentioned) > 0


class FileIdNotFoundException(Exception):
    pass


class FileNameNotFoundException(Exception):
    pass


class DateNotFoundException(Exception):
    pass


class RootFolderDoesNotExistException(Exception):
    pass


class CommentIsEmptyException(Exception):
    pass

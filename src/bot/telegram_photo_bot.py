import logging
import pathlib
from pathlib import Path
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from bot.date_utils import DateUtil

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)


class PhotoBot:
    def __init__(self, root_dir) -> None:
        self._logger = logging.getLogger(__name__)
        self._root_dir = root_dir

    def receiveUpdate(self, update: Update, context: CallbackContext) -> None:
        self._logger.info(update)
        update_file_name, update_file_id, update_comment = None, None, None
        if update.message.document:
            update_file_name = update.message.document.file_name
            update_file_id = update.message.document.file_id
            update_comment = update.message.caption

        if not update_file_name or not update_file_id or not update_comment:
            return
        try:
            path = self.makeDirForPost(update_file_name, update_comment)
            full_local_name = path + "/" + update_file_name
            self.downloadFile(context, update_file_id, full_local_name)
        except DateNotFoundException:
            update.message.reply_text("Не смог найти дату события")
        except FileNotFoundError:
            update.message.reply_text("Не смог сохранить файл")

        # update.message.reply_text(update.message.text)

    def makeDirForPost(self, update_file_name: str, update_comment: str):

        post_dir = None
        if DateUtil.isStartWithDate(update_comment):
            post_dir = update_comment

        if not post_dir and DateUtil.isContainRawDate(update_file_name):
            post_dir = DateUtil.makeDateString(update_file_name) + " " + update_comment

        # if not date_part_of_dir:
        # tryGetDateFromMultipost()
        #    pass
        if not post_dir:
            raise DateNotFoundException('Date not found in post data')

        if not Path(self._root_dir).is_dir():
            raise RootFolderDoesNotExist

        full_path = self._root_dir + "/" + post_dir
        if not Path(full_path).is_dir():
            Path(full_path).mkdir()
        return full_path

    def downloadFile(self, context, update_file_id, full_local_name):
        context.bot.getFile(update_file_id).download(full_local_name)


class DateNotFoundException(Exception):
    pass


class RootFolderDoesNotExist(Exception):
    pass


def main() -> None:
    bot = PhotoBot("/tmp/photo")
    updater = Updater("2033916236:AAFQ1EyIG8oZbNF_XACGqYkKuepvqH8Cpuc")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, bot.receiveUpdate))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

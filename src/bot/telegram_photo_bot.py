import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)


class FileDownloader:
    def downloadFile(self, context, full_local_name, update_file_id):
        context.bot.getFile(update_file_id).download(full_local_name)


class PhotoBot:
    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)

    def receiveUpdate(self, update: Update, context: CallbackContext) -> None:
        self._logger.info(update)
        if update.message.document:
            self._logger.info("Received file {} with id {}".format(update.message.document.file_name, update.message.document.file_id))

            path = '/tmp/photo'
            name = update.message.document.file_name
            full_local_name = path + "/" + name

            update_file_id = update.message.document.file_id

            self.downloadFile(context, update_file_id, full_local_name)

        # update.message.reply_text(update.message.text)

    def downloadFile(self, context, update_file_id, full_local_name):
        context.bot.getFile(update_file_id).download(full_local_name)


def main() -> None:
    bot = PhotoBot()
    updater = Updater("2033916236:AAFQ1EyIG8oZbNF_XACGqYkKuepvqH8Cpuc")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, bot.receiveUpdate))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


if __name__ == '__main__':
    main()

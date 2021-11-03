import getopt
import logging
import sys

from telegram.ext import Updater, MessageHandler, Filters
from bot.telegram_photo_bot import PhotoBot

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)


def main(argv) -> None:
    logger = logging.getLogger(__name__)
    help_string = 'run.py \n' \
                  '-k, --key <api key>\n' \
                  '-p, --path <root path for files>'

    try:
        opts, args = getopt.getopt(argv, "hk:p:", ["key=", "path="])
        if len(opts) == 0 or len(opts) > 2:
            print(help_string)
            sys.exit(2)
    except getopt.GetoptError:
        print(help_string)
        sys.exit(2)

    api_key, root_path = None, None

    for opt, arg in opts:
        if opt == '-h':
            print(help_string)
            sys.exit()
        elif opt in ("-k", "--key"):
            api_key = arg
        elif opt in ("-p", "--path"):
            root_path = arg

    logger.info("Start with key={} and path={}".format(api_key, root_path))

    bot = PhotoBot(root_path)
    updater = Updater(api_key)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, bot.receiveUpdate))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main(sys.argv[1:])

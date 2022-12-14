import os

from config.get_keys import Config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import Responses as R

TELEGRAM_API_KEY = Config.API_KEY
PORT = int(os.environ.get('PORT', '8443'))

print("Bot started...")


def start_command(update, context):
    update.message.reply_text('Type something random to get started!')


def help_command(update, context):
    update.message.reply_text('Help!')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)
    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(TELEGRAM_API_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TELEGRAM_API_KEY,
                          webhook_url='https://ktktoolsbot.herokuapp.com/' + TELEGRAM_API_KEY)
    updater.idle()


if __name__ == '__main__':
    main()

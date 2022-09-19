from telegram.ext import Updater, CommandHandler, CallbackContext
import re

TELEGRAM_TOKEN = '5571332182:AAHqhLezaegi1_AtqXoVFF4u_iiFugZuSwE'
json = {"dish": "яичница с беконом", "type": "завтрак", "ingredients": [ "яйцо", "бекон"]}



def dish(update, context):
    """
    Greet the user with their first name and Telegram ID.
    """
    user_message = update.message.text
    m = re.search(r'/dish -t \w+ -i [\w+, ]+', update.message.text)
    print(m[0])

    return update.message.reply_text(
        re.search(r'-t \w+', update.message.text)[0][3:]
    )


if __name__ == '__main__':
    updater = Updater(TELEGRAM_TOKEN)

    updater.dispatcher.add_handler(
        CommandHandler('dish', dish)
    )

    updater.start_polling()
    updater.idle()

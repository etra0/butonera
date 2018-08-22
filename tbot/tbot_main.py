import requests, os
from telegram import ext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from .secret_token import token


def get_sounds():
    extensions = ('mp3', 'wav', 'ogg')
    return {f.split('.')[0]: f for f in os.listdir("./static/sounds/") if f.endswith(extensions)}

def run_tbot(ip):
    updater = ext.Updater(token=token)

    for key, value in get_sounds().items():
        updater.dispatcher.add_handler(
            ext.CommandHandler(
                key, lambda bot, update: requests.get(
                    'http://{}:5000/play_sound/{}'.format(
                        ip, value
                    )
                )
            )
        )

    def start(bot, update):
        keyboard = [
            [InlineKeyboardButton(key, callback_data=value)] for key, value in get_sounds().items()
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Buttons', reply_markup=reply_markup)

    def button(bot, update):
        query = update.callback_query
        requests.get('http://{}:5000/play_sound/{}'.format(ip, query.data))
        bot.edit_message_text(text="sent: {}".format(query.data),
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)

    updater.dispatcher.add_handler(ext.CallbackQueryHandler(button))
    updater.dispatcher.add_handler(ext.CommandHandler('start', start))

    updater.start_polling()

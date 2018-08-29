import requests, os
from telegram import ext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from .secret_token import token


def get_sounds():
    extensions = ('mp3', 'wav', 'ogg')
    return {f.split('.')[0]: f for f in os.listdir("./static/sounds/") if f.endswith(extensions)}


def run_tbot(ip):
    updater = ext.Updater(token=token)
    sounds = get_sounds()
    sound_keys = sorted(list(sounds.keys()))

    def generic(bot, update):
        sound = sounds[update.message.text[1:]]
        requests.get('http://{}:5000/play_sound/{}'.format(ip, sound))
        bot.send_message(chat_id=update.message.chat_id, text='sent: {}'.format(sound))

    def play(bot, update):
        keyboard = [
            [
                InlineKeyboardButton(sound_keys[2*i], callback_data=sounds[sound_keys[2*i]]),
                InlineKeyboardButton(sound_keys[2*i+1], callback_data=sounds[sound_keys[2*i+1]]) \
                if 2*i+1 < len(sound_keys) else InlineKeyboardButton('', callback_data=sounds[sound_keys[2*i]]),
            ] for i in range((len(sound_keys) +1 ) //2)
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Buttons:', reply_markup=reply_markup)

    def button(bot, update):
        query = update.callback_query
        requests.get('http://{}:5000/play_sound/{}'.format(ip, query.data))
        bot.edit_message_text(text="sent: {}".format(query.data),
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)

    updater.dispatcher.add_handler(ext.CallbackQueryHandler(button))
    updater.dispatcher.add_handler(ext.CommandHandler('play', play))
    for key in sound_keys:
        updater.dispatcher.add_handler(ext.CommandHandler(key, generic))

    updater.start_polling()

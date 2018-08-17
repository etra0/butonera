import requests
from telegram import ext
from secret_token import token

ip_addr = 'localhost'

updater = ext.Updater(token=token)
dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='set ip: /ip <ip>\nplay: /play <button>')
start_handler = ext.CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def ip(bot, update):
    global ip_addr
    ip_addr = update.message.text.split()[-1]
    bot.send_message(chat_id=update.message.chat_id, text='ip set to {}'.format(ip_addr))
ip_handler = ext.CommandHandler('ip', ip)
dispatcher.add_handler(ip_handler)

def play(bot, update):
    extensions = ('mp3', 'wav', 'ogg')
    for type in extensions:
        try:
            requests.get('http://{}:5000/play_sound/{}.{}'.format(ip_addr, update.message.text.split()[-1], type))
        except:
            pass
    bot.send_message(chat_id=update.message.chat_id, text='send')
play_handler = ext.CommandHandler('play', play)
dispatcher.add_handler(play_handler)

updater.start_polling()

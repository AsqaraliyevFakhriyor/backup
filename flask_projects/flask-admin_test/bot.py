import threading
from app import User
import telebot

TOKEN = '1503648543:AAFH1n8Dx3iEwpMnMwFtu3bmhW456JTxw0o'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def command_help(message):
    name = message.from_user.first_name
    user_tg_id = message.from_user.id
    new_user = User(name=name, user_tg_id=user_tg_id)
    new_user.insert()
    bot.reply_to(message, "name: {}, id: {}, saved successfully!".format(name, user_tg_id))


if __name__ == '__main__':
    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()
    bot.polling(threading=True,none_stop=True)
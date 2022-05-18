import telebot
from telebot import TeleBot

TOKEN = "5313606339:AAGQK-c56x13G3bA-nJzDr-WXNkRjXuW-F4"

bot: TeleBot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Приветствую, {message.chat.username}")

@bot.message_handler(content_types=['photo',])
def massage_photo(message: telebot.types.Message):
    bot.reply_to(message,'Nice meme XDD')

bot.polling(none_stop=True)
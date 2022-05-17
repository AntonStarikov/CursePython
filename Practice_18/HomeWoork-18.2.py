import telebot

TOKEN = "5313606339:AAGQK-c56x13G3bA-nJzDr-WXNkRjXuW-F4"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(filters)
def function_name(message):
    bot.reply_to(message, "This is a message handler")

bot.polling(none_stop=True)
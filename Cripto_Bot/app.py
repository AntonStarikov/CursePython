import telebot


TOKEN = "5382817722:AAFAHHnwpJ3qcJW08Sblt0CG_JodXoWKfTo"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Привет')

bot.polling()
import telebot

bot = telebot.TeleBot('6237509767:AAFU24YJIk4qehVbEDFkrXalCatw8QdB6M4')

@bot.message_handler(commands=['start', 'help'])



def get_text_messages(message):
    bot.send_message(message.from_user.id, "пришли ссылку.")
    return message


bot.polling(none_stop=True, interval=0)

url = get_text_messages
print(url)
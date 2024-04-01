import telebot

token = "7089778467:AAFhooMbonuxewUf4NEXASknme2YIN8n-Yw"
id_channel = "@aefeawfawefaewafaewfw"
bot = telebot.Telebot(token)

@bot.message_handler(content_types=['text'])
def commands(message):
    bot.send_message(id_channel, message.text)

bot.polling()
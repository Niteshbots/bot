import telebot
bot = telebot.Telebot("1244021573:AAEakjjhchvuB7RPQ5-fEZ46w46GcSsNS88")
@bot.message.handler(content_types=["text"])
def repeat_all_messages(message):
	bot.send_message(message.chat.id, message.text)
	
if __name__ == '__main__':
	bot.polling(nonstop=true)
	
	

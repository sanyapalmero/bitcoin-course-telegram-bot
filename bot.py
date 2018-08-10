import telebot
import config
import requests
import json

bot = telebot.TeleBot(config.token)

def get_course():
    url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC&tsyms=USD,EUR,RUR"
    str_json = requests.get(url)
    parsed_json = json.loads(str_json.text)
    rur = parsed_json["BTC"]["RUR"]
    eur = parsed_json["BTC"]["EUR"]
    usd = parsed_json["BTC"]["USD"]
    course = f"1 биткоин равен {rur} рублям, {eur} евро, {usd} долларов"
    return course

@bot.message_handler(commands=['get'])
def get(message):
    course = get_course()
    bot.send_message(message.chat.id, course)

bot.polling()

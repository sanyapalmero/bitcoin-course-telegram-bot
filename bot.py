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
    course = f"1₿ = {rur}₽\n1₿ = {eur}€\n1₿ = {usd}$"
    return course

@bot.message_handler(commands=['get'])
def get(message):
    course = get_course()
    bot.send_message(message.chat.id, course)

@bot.message_handler(commands=['start'])
def start(message):
    start_message = "Добро пожаловать. Bitcoin Course Bot - бот, который покажет вам курс биткоина в рублях, долларах и евро.\nВведите /help чтобы узнать возможности бота"
    bot.send_message(message.chat.id, start_message)

@bot.message_handler(commands=['help'])
def get_help(message):
    commands = "/help - список комманд\n/get - получить текущий курс биткоина"
    bot.send_message(message.chat.id, commands)

bot.polling()

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests
import io


TOKEN = "5943242364:AAEDa7ko4pgcCKnzSOw7WdvU8eYMH8OWD6M"

bot = telebot.TeleBot(token=TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def welcome_message(message):
    welcome_message = "Привет. Этот бот достает фотки кошек из интенета!"

    bot.reply_to(message, welcome_message, reply_markup=keyboard())


@bot.message_handler(content_types=['text'])
def message_handle(message):
    if message.text == "Дай кота!":
        cat = get_cat()
        bot.send_photo(message.chat.id, cat)
        bot.send_document(message.chat.id, cat)


def keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton("Дай кота!")
    keyboard.add(button)

    return keyboard


def get_cat():

    zagalovki = {"contect-type": "image/jpeg"}
    reply = requests.get("https://thiscatdoesnotexist.com/", headers=zagalovki)

    image = reply.content
    image = io.BytesIO(image)

    image.
    return image

bot.infinity_polling()
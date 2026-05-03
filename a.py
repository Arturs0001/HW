import telebot
import os
import random
import string
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))

@bot.message_handler(commands=['start'])
def start(message):
    kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("Rock", "Scissors", "Paper")
    bot.send_message(message.chat.id, "Send a number(password generator), ask a question(?), or play(rsp)", reply_markup=kb)

@bot.message_handler(func=lambda m: True)
def all(message):
    text = message.text

    if text in ["Rock", "Scissors", "Paper"]:
        bot_choice = random.choice(["Rock", "Scissors", "Paper"])

        if text == bot_choice:
            result = "Draw"
        elif (text == "Rock" and bot_choice == "Scissors") or \
             (text == "Scissors" and bot_choice == "Paper") or \
             (text == "Paper" and bot_choice == "Rock"):
            result = "You win"
        else:
            result = "I win"

        bot.send_message(message.chat.id, f"{text} vs {bot_choice}\n{result}")

    elif text.isdigit():
        password = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%") for _ in range(int(text)))
        bot.send_message(message.chat.id, password)

    elif "?" in text:
        bot.send_message(message.chat.id, random.choice([
            "Yes", "No", "Maybe", "Try again", "Definitely"
        ]))

    else:
        bot.send_message(message.chat.id, "I don't understand")

bot.infinity_polling()


if __name__ == "__main__":
    print('Bot is running . . . ')
    bot.infinity_polling()


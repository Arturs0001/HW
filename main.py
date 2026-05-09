import telebot
import os
import re
from dotenv import load_dotenv
from telebot import types
from telebot import custom_filters
from telebot.storage import StateMemoryStorage
from telebot.states import State, StatesGroup

load_dotenv()

TOKEN = os.getenv('TOKEN')

if not TOKEN:
    print('Token not found!')
    exit()

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(TOKEN, state_storage=state_storage)

bot.add_custom_filter(custom_filters.StateFilter(bot))


class RegistrationStates(StatesGroup):
    waiting_for_email = State()
    waiting_for_phone = State()


reg_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
reg_kb.add(types.KeyboardButton('Реєстрація ✔'))

cancel_kb = types.InlineKeyboardMarkup()
cancel_kb.add(types.InlineKeyboardButton('Скасувати', callback_data='cancel'))

remove_kb = types.ReplyKeyboardRemove()


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(
        message.chat.id,
        'Привіт! Натисни "Реєстрація" щоб почати.',
        reply_markup=reg_kb
    )


@bot.message_handler(func=lambda message: message.text == 'Реєстрація ✔')
def start_registration(message):
    bot.send_message(
        message.chat.id,
        '⌛ Оновлюємо інтерфейс...',
        reply_markup=remove_kb
    )

    bot.set_state(
        message.from_user.id,
        RegistrationStates.waiting_for_email,
        message.chat.id
    )

    bot.send_message(
        message.chat.id,
        'Введи свою електронну пошту:',
        reply_markup=cancel_kb
    )


@bot.message_handler(state=RegistrationStates.waiting_for_email)
def process_email(message):
    email = message.text
    email_pattern = r"^[\w\.-_]+@[\w\.-_]+\.\w+$"

    if not re.match(email_pattern, email):
        bot.send_message(
            message.chat.id,
            'Невірний email. Спробуй ще раз.'
        )
        return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['email'] = email

    bot.set_state(
        message.from_user.id,
        RegistrationStates.waiting_for_phone,
        message.chat.id
    )

    bot.send_message(
        message.chat.id,
        'Введи номер телефону (наприклад: +380XXXXXXXXX):',
        reply_markup=remove_kb
    )


@bot.message_handler(state=RegistrationStates.waiting_for_phone)
def process_phone(message):
    phone_number = message.text
    phone_pattern = r"^\+?\d{10,15}$"

    if not re.match(phone_pattern, phone_number):
        bot.send_message(
            message.chat.id,
            'Невірний формат номера. Спробуй ще раз.'
        )
        return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        email = data.get('email')

    with open('users.txt', 'a') as f:
        f.write(f"{email} | {phone_number}\n")

    bot.delete_state(message.from_user.id, message.chat.id)

    bot.send_message(
        message.chat.id,
        'Реєстрація завершена!',
        reply_markup=reg_kb
    )


@bot.callback_query_handler(func=lambda call: call.data == 'cancel')
def cancel_handler(call):
    bot.delete_state(call.from_user.id, call.message.chat.id)

    bot.send_message(
        call.message.chat.id,
        'Реєстрацію скасовано.',
        reply_markup=reg_kb
    )

    bot.answer_callback_query(call.id)


if __name__ == "__main__":
    print('Bot is running...')
    bot.infinity_polling()
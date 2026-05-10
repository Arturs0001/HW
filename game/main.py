import telebot
import os
import random
from dotenv import load_dotenv
from telebot import types

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

games = {}


def create_board():
    return [" " for _ in range(9)]


def create_keyboard(board):
    keyboard = types.InlineKeyboardMarkup(row_width=3)

    buttons = []

    for i in range(9):
        buttons.append(
            types.InlineKeyboardButton(
                text=board[i],
                callback_data=f"move_{i}"
            )
        )

    keyboard.add(*buttons)

    return keyboard


def check_winner(board, symbol):
    win_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    for pos in win_positions:
        if (
            board[pos[0]] == symbol and
            board[pos[1]] == symbol and
            board[pos[2]] == symbol
        ):
            return True

    return False


def board_full(board):
    return " " not in board


@bot.message_handler(commands=["start"])
def start(message):

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
        types.InlineKeyboardButton(
            "Play as X",
            callback_data="symbol_X"
        ),

        types.InlineKeyboardButton(
            "Play as O",
            callback_data="symbol_O"
        )
    )

    bot.send_message(
        message.chat.id,
        "Choose your symbol:",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("symbol_"))
def choose_symbol(call):

    player_symbol = call.data.split("_")[1]

    if player_symbol == "X":
        bot_symbol = "O"
    else:
        bot_symbol = "X"

    games[call.message.chat.id] = {
        "board": create_board(),
        "player": player_symbol,
        "bot": bot_symbol
    }

    board = games[call.message.chat.id]["board"]

    bot.edit_message_text(
        "Game started!",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=create_keyboard(board)
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("move_"))
def make_move(call):

    game = games.get(call.message.chat.id)

    if not game:
        return

    board = game["board"]

    position = int(call.data.split("_")[1])

    if board[position] != " ":
        bot.answer_callback_query(
            call.id,
            "Cell already used!"
        )
        return

    board[position] = game["player"]

    if check_winner(board, game["player"]):

        bot.edit_message_text(
            "You win!",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=create_keyboard(board)
        )

        del games[call.message.chat.id]
        return

    if board_full(board):

        bot.edit_message_text(
            "Draw!",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=create_keyboard(board)
        )

        del games[call.message.chat.id]
        return

    empty_positions = []

    for i in range(9):
        if board[i] == " ":
            empty_positions.append(i)

    bot_move = random.choice(empty_positions)

    board[bot_move] = game["bot"]

    if check_winner(board, game["bot"]):

        bot.edit_message_text(
            "Bot wins!",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=create_keyboard(board)
        )

        del games[call.message.chat.id]
        return

    if board_full(board):

        bot.edit_message_text(
            "Draw!",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=create_keyboard(board)
        )

        del games[call.message.chat.id]
        return

    bot.edit_message_reply_markup(
        call.message.chat.id,
        call.message.message_id,
        reply_markup=create_keyboard(board)
    )


print("Bot is running...")
bot.infinity_polling()
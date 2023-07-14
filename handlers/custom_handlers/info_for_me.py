from telebot.types import Message

from config_data.config import LINK_TO_GITHUB, LINK_TO_VIDEO, MY_INFO
from keyboards.reply.reply_kb import (
    TEXT_FOR_ANSWER,
    TEXT_FOR_ANSWER_VOICE,
    answer_for_photo,
    answer_for_voice,
)
from loader import bot
from utils.utils import get_message


@bot.message_handler(
    commands=["my_info"],
)
@bot.callback_query_handler(func=lambda call: call.data == "my_info")
def my_info(data):
    message = get_message(data)
    bot.send_message(message.chat.id, MY_INFO)


@bot.message_handler(
    commands=["get_link_this_bot"],
)
@bot.callback_query_handler(func=lambda call: call.data == "get_link_this_bot")
def get_link_this_bot(data):
    message = get_message(data)
    bot.send_message(message.chat.id, LINK_TO_GITHUB)


@bot.message_handler(
    commands=["look_photo"],
)
@bot.callback_query_handler(func=lambda call: call.data == "look_photo")
def get_photo(data):
    message = get_message(data)
    bot.send_message(
        message.chat.id,
        "Какое фото нужно посмотреть?",
        reply_markup=answer_for_photo(),
    )
    bot.register_next_step_handler(message, results_photo)


def results_photo(message):
    if message.text == TEXT_FOR_ANSWER[0][0]:
        photo = open(TEXT_FOR_ANSWER[0][1], "rb")
    elif message.text == TEXT_FOR_ANSWER[1][0]:
        photo = open(TEXT_FOR_ANSWER[1][1], "rb")
    else:
        remove_keyboard(message, TEXT_FOR_ANSWER[2][1])
        return

    bot.send_photo(message.chat.id, photo)
    photo.close()
    get_photo(message)


@bot.message_handler(commands=["get_voice"])
@bot.callback_query_handler(func=lambda call: call.data == "get_voice")
def get_voice(data):
    message = get_message(data)
    bot.send_message(
        message.chat.id, "Что хочешь послушать?", reply_markup=answer_for_voice()
    )
    bot.register_next_step_handler(message, results_voice)


def results_voice(message):
    if message.text == TEXT_FOR_ANSWER_VOICE[0][0]:
        audio = open(TEXT_FOR_ANSWER_VOICE[0][1], "rb")
    elif message.text == TEXT_FOR_ANSWER_VOICE[1][0]:
        audio = open(TEXT_FOR_ANSWER_VOICE[1][1], "rb")
    elif message.text == TEXT_FOR_ANSWER_VOICE[2][0]:
        audio = open(TEXT_FOR_ANSWER_VOICE[2][1], "rb")
    else:
        remove_keyboard(message, TEXT_FOR_ANSWER_VOICE[3][1])
        return

    bot.send_audio(message.chat.id, audio)
    if message.text == TEXT_FOR_ANSWER_VOICE[2][0]:
        bot.send_message(message.chat.id, LINK_TO_VIDEO)
    audio.close()
    get_voice(message)


def remove_keyboard(message, reply_markup_remove):
    bot.send_message(
        message.from_user.id,
        "Что еще хотите узнать?",
        reply_markup=reply_markup_remove(),
    )

from telebot.types import Message, ReplyKeyboardRemove

from config_data.config import MY_INFO
from keyboards.reply.reply_kb import (TEXT_FOR_ANSWER, TEXT_FOR_ANSWER_VOICE,
                                      answer_for_photo, answer_for_voice)
from loader import bot


@bot.message_handler(
    commands=["my_info"],
)
def my_info(message: Message) -> None:

    bot.send_message(message.from_user.id, MY_INFO)


@bot.message_handler(
    commands=["look_photo"],
)
def get_photo(message: Message) -> None:

    bot.send_message(
        message.from_user.id,
        "Какое фото нужно посмотреть?",
        reply_markup=answer_for_photo(),
    )
    bot.register_next_step_handler(message, results_photo)


def results_photo(message: Message) -> None:
    if message.text == TEXT_FOR_ANSWER[0][0]:
        photo = open(TEXT_FOR_ANSWER[0][1], "rb")
    else:
        photo = open(TEXT_FOR_ANSWER[1][1], "rb")

    bot.send_photo(message.from_user.id, photo)
    photo.close()
    remove_keyboard(message)


@bot.message_handler(commands=["get_voice"])
def get_voice(message: Message) -> None:

    bot.send_message(
        message.from_user.id, "Что хочешь послушать?", reply_markup=answer_for_voice()
    )
    bot.register_next_step_handler(message, results_voice)


def results_voice(message: Message) -> None:
    if message.text == TEXT_FOR_ANSWER_VOICE[0][0]:
        audio = open(TEXT_FOR_ANSWER_VOICE[0][1], "rb")
    elif message.text == TEXT_FOR_ANSWER_VOICE[1][0]:
        audio = open(TEXT_FOR_ANSWER_VOICE[1][1], "rb")
    else:
        audio = open(TEXT_FOR_ANSWER_VOICE[2][1], "rb")

    bot.send_audio(message.chat.id, audio)
    audio.close()
    remove_keyboard(message)


def remove_keyboard(message):
    bot.send_message(
        message.from_user.id, "Что дальше?", reply_markup=ReplyKeyboardRemove()
    )

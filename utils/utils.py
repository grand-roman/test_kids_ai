from telebot.types import CallbackQuery, Message


def get_message(data):
    if isinstance(data, Message):
        return data
    elif isinstance(data, CallbackQuery):
        return data.message

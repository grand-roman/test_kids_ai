from functools import wraps

from telebot.types import CallbackQuery, Message

from loader import bot


def get_message(data):
    if isinstance(data, Message):
        return data
    elif isinstance(data, CallbackQuery):
        return data.message


def send_action(action):
    def decorator(func):
        @wraps(func)
        def command_func(update, context, *args, **kwargs):
            chat_id = update.from_user.id
            bot.send_chat_action(chat_id=chat_id, action=action)
            return func(update, context, *args, **kwargs)

        return command_func

    return decorator

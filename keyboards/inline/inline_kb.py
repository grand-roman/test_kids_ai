from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_button(items):
    kb = InlineKeyboardMarkup(row_width=1)
    for command, desk in items:
        btn = InlineKeyboardButton(text=desk, callback_data=command)
        kb.add(btn)
    return kb

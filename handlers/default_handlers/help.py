from config_data.config import DEFAULT_COMMANDS
from keyboards.inline.inline_kb import create_button
from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message):
    kb = create_button(DEFAULT_COMMANDS[2:])
    bot.send_message(message.from_user.id, "Команды бота:", reply_markup=kb)


@bot.message_handler(commands=["nextstep"])
def next_step(message):
    text = "Чтобы лучше понять тебе как устроен бот вызови команду /help"
    bot.reply_to(message, text)

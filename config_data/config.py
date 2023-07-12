import os

from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("look_photo", "Посмотреть фото"),
    ("my_info", "Информация обо мне"),
    ("get_voice", "Голосовые ответы"),
    ("get_link_this_bot", "Ссылка на проект"),
)

MY_INFO = (
    "Добрый день\n"
    "Меня зовут Роман Андреев, я ведущий Backend "
    "разработчик в Умскул.\nОсновной стек это python,"
    "Django, ML, docker.\nИмею опыт в преподавании с "
    "2019 года.\nВ 2020 году открывал свою онлайн школу "
    "по программированию на языке python и c++.\n"
    "Насладись обилием полезной информации.\n"
    "И самое главное – пишите код в своё удовольствие.\n"
    "А я буду тебе в этом помогать!"
)

LINK_TO_GITHUB = "https://github.com/grand-roman/test_kids_ai"

LANGUAGE = "ru_RU"

PATH_FOR_VOICE = "voice/recognise/voice/"

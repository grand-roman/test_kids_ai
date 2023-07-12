from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

TEXT_FOR_ANSWER = [
    [
        "Мое последнее селфи",
        "photo/1.jpeg",
    ],
    [
        "Фото из старшей школы",
        "photo/2.jpg",
    ],
    [
        "Выйти",
        ReplyKeyboardRemove,
    ],
]

TEXT_FOR_ANSWER_VOICE = [
    [
        "Рассказ в формате «объясняю своей бабушке», что такое GPT",
        "voice/test.mp3",
    ],
    [
        "Максимально коротко объясняю разницу между SQL и NoSQL",
        "voice/test.mp3",
    ],
    [
        "История первой любви",
        "voice/test.mp3",
    ],
    [
        "Выйти",
        ReplyKeyboardRemove,
    ],
]


def answer_for_photo():
    rkb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kbs = [KeyboardButton(text=kb_text) for kb_text, _ in TEXT_FOR_ANSWER]
    rkb.add(*kbs)

    return rkb


def answer_for_voice():
    rkb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kbs = [KeyboardButton(text=kb_text) for kb_text, _ in TEXT_FOR_ANSWER_VOICE]
    rkb.add(*kbs)

    return rkb

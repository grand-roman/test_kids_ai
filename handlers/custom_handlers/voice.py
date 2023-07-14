import json
import os
import subprocess
import urllib.request
import uuid

import speech_recognition as sr
from telegram.constants import ChatAction

from config_data.config import DEFAULT_COMMANDS, LANGUAGE, PATH_FOR_VOICE
from loader import bot, recognizer
from utils.utils import send_action


def recognise(filename):
    with sr.AudioFile(filename) as source:
        audio_text = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_text, language=LANGUAGE)
            print(text)
            return text
        except:
            return "Извините, я вас не понял"


def gen_request(text):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 "
        "(KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Origin": "https://yandex.ru",
        "Referer": "https://yandex.ru/",
    }

    api_url = "https://yandex.ru/lab/api/yalm/text3"
    payload = {"query": text, "intro": 0, "filter": 1}
    params = json.dumps(payload).encode("utf8")
    req = urllib.request.Request(api_url, data=params, headers=headers)
    response = urllib.request.urlopen(req)
    text = response.read().decode("unicode-escape")
    text_first = 'text": "'
    begin = text.find(text_first)
    end = text.find('", "is_cached"')
    text = text[begin:end]
    if not text:
        text = "Походу балабола поломалась"
    else:
        text = text[len(text_first) :]
    return text


@send_action(ChatAction.TYPING)
def answer_bot(message, text):
    response_text = gen_request(text)
    bot.send_message(message.from_user.id, response_text)


@bot.message_handler(content_types=["voice"])
def voice_processing(message):
    filename = str(uuid.uuid4())
    file_name_full = PATH_FOR_VOICE + filename
    file_name_full_ogg = f"{file_name_full}.ogg"
    file_name_full_wav = f"{file_name_full}.wav"

    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open(file_name_full_ogg, "wb") as new_file:
        new_file.write(downloaded_file)

    subprocess.run(["ffmpeg", "-y", "-i", file_name_full_ogg, file_name_full_wav])
    text = recognise(file_name_full_wav)

    bot.reply_to(message, text)
    os.remove(file_name_full_ogg)
    os.remove(file_name_full_wav)
    answer_bot(message, text)

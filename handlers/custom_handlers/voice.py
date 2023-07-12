import os
import subprocess
import uuid

import speech_recognition as sr

from config_data.config import DEFAULT_COMMANDS, LANGUAGE, PATH_FOR_VOICE
from loader import bot, recognizer


def recognise(filename):
    with sr.AudioFile(filename) as source:
        audio_text = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_text, language=LANGUAGE)
            print(text)
            return text
        except:
            return "Извините, я вас не понял"


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
    call_command = "/"

    for command, desk in DEFAULT_COMMANDS:
        if text in desk.lower():
            call_command += command
            break

    bot.reply_to(message, text)
    bot.send_message(message.from_user.id, call_command)
    # bot.
    os.remove(file_name_full_ogg)
    os.remove(file_name_full_wav)

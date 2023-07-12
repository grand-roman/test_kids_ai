import speech_recognition
from telebot import TeleBot
from telebot.storage import StateMemoryStorage

from config_data import config

storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)
recognizer = speech_recognition.Recognizer()

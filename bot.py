import telebot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Selamat datang ke AutoBot! 👋")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Awak hantar: {message.text}")

print("Bot sedang berjalan... Tekan Ctrl + C untuk berhenti.")
bot.infinity_polling()

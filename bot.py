import telebot
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Selamat datang ke AutoBot! 👋")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Awak hantar: {message.text}")

print("Bot sedang berjalan... Tekan Ctrl + C untuk berhenti.")
bot.infinity_polling()

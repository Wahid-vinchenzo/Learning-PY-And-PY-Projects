import telebot
import requests
from telebot import types

API_TOKEN = 'use your own api'  # Replace with your bot token
OPENROUTER_API_KEY = 'use your own'  # Replace with your API key
MODEL = 'openai/gpt-3.5-turbo'

VALID_PASSWORDS = ['111111', '12345', '12345']
AUTHORIZED_USERS = set()
USER_HISTORY = {}  # user_id => list of messages

bot = telebot.TeleBot(API_TOKEN)

# Menu keyboard
def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('💬 Chat', '❌ Exit')
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if user_id in AUTHORIZED_USERS:
        bot.send_message(message.chat.id,
                         "✅ You're already authorized. Choose an option below:",
                         reply_markup=get_main_menu())
    else:
        bot.send_message(message.chat.id,
                         "🔒 This bot is private.\nPlease enter the password to access:")

@bot.message_handler(func=lambda message: message.from_user.id not in AUTHORIZED_USERS)
def check_password(message):
    user_id = message.from_user.id
    if message.text.strip() in VALID_PASSWORDS:
        AUTHORIZED_USERS.add(user_id)
        USER_HISTORY[user_id] = []  # Initialize chat history
        bot.send_message(message.chat.id,
                         "✅ Access granted!\nChoose an option below:",
                         reply_markup=get_main_menu())
    else:
        bot.send_message(message.chat.id, "❌ Incorrect password. Try again.")

@bot.message_handler(func=lambda message: message.from_user.id in AUTHORIZED_USERS)
def respond_to_message(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    user_message = message.text.strip()

    if user_message == '❌ Exit':
        bot.send_message(chat_id, "👋 Goodbye!", reply_markup=types.ReplyKeyboardRemove())
        return

    elif user_message == '💬 Chat':
        bot.send_message(chat_id, "💬 Send your message now and I will respond.")
        return

    # Initialize user history if not already
    if user_id not in USER_HISTORY:
        USER_HISTORY[user_id] = []

    # Add user message to history
    USER_HISTORY[user_id].append({"role": "user", "content": user_message})

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": MODEL,
                "messages": USER_HISTORY[user_id]  # Full chat history
            }
        )

        if response.status_code == 200:
            reply = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
            # Add bot reply to history
            USER_HISTORY[user_id].append({"role": "assistant", "content": reply})
        else:
            reply = "⚠️ Error: Problem with the AI service."

    except Exception as e:
        reply = f"❗ An error occurred: {e}"

    bot.send_message(chat_id, reply)

bot.polling()

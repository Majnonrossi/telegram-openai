import requests
import telebot

TELEGRAM_BOT_TOKEN = '6630514763:AAEllHZ6H_etDV6OaLMFHF0vU5iolJeBiNY'

def get_chatgpt_response(text):
    CHATGPT_API_URL = f'https://botz-openai-prod-botz-chatgpt-s78su6.mo1.mogenius.io/chatgpt?text={text}'
    response = requests.get(CHATGPT_API_URL)
    return response.json()['result']

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text
    chatgpt_response = get_chatgpt_response(user_text)
    bot.send_message(message.chat.id, chatgpt_response)

bot.polling()

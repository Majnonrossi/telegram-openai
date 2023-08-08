import requests
import telebot
import threading

TELEGRAM_BOT_TOKEN = '6630514763:AAEllHZ6H_etDV6OaLMFHF0vU5iolJeBiNY'

def get_chatgpt_response(text):
    CHATGPT_API_URL = f'https://botz-openai-prod-botz-chatgpt-s78su6.mo1.mogenius.io/chatgpt?text={text}'
    response = requests.get(CHATGPT_API_URL)
    return response.json()['result']

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def send_waiting_message(chat_id):
    waiting_message = "جارٍ توليد الإجابة... 🔄"
    bot.send_message(chat_id, waiting_message)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text
    chat_id = message.chat.id

    # إظهار رسالة انتظار للمستخدم
    waiting_thread = threading.Thread(target=send_waiting_message, args=(chat_id,))
    waiting_thread.start()

    # الحصول على الإجابة من ChatGPT
    chatgpt_response = get_chatgpt_response(user_text)

    # إرسال الإجابة النهائية للمستخدم
    bot.send_message(chat_id, chatgpt_response + '\n\n- D𝐞𝐯 >> 𝐝𝐚𝐫𝐤 𝐦𝐚𝐧\n- @darkman_fit')

bot.polling()

import os
import telebot
from openai import OpenAI

bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@bot.message_handler(func=lambda m: True)
def reply(m):
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": m.text}]
    )
    bot.reply_to(m, resp.choices[0].message.content)

print("Bot LIVE")
bot.infinity_polling()

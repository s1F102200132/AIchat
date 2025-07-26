from django.shortcuts import render
from django.http import HttpResponse

# --- ChatterBot関連 ---
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chatbot', read_only=False,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
        }
    ]
)

list_to_train = [
    "hi", "hi, there",
    "what's your name?", "I'm just a chatbot",
    "what is your favorite food?", "i like cheese",
    "what's your favorite sport?", "swimming",
    "do you have children?", "no",
    "こんにちは", "こんにちは！！"
]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)
# chatterbotCorpusTrainer.train('chatterbot.corpus.english')  # 必要に応じて有効化

# --- OpenAI関連 ---
import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # .env から環境変数を読み込む
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai.api_key)

# --- Djangoビュー ---
def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    return HttpResponse("list1")

def getResponse(request):
    user_message = request.GET.get('userMessage', '')
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは親切な飲食店サポートチャットボットです。"},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message.content.strip()
        return HttpResponse(reply)

    except Exception as e:
        return HttpResponse(f"エラーが発生しました: {e}")

def chatbot_iframe(request):
    return render(request, 'blog/chat_iframe.html')

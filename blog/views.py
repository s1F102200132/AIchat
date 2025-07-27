from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chatbot',read_only=False,
                logic_adapters=[
                    {
                        
                        'import_path':'chatterbot.logic.BestMatch'
                        #'default_response':'Sorry, I dont know what that means',
                        #'maximun_similarity_threshold':0.90
                    
                    }
                    ])

list_to_train = [
     
      "hi",
      "hi, there",
      "what's your name?",
      "I'm just a chatbot",
      "what is your favorite food?",
      "i like cheese",
      "what's your favorite sport?",
      "swimming",
      "do you have children?",
      "no",
      "こんにちは",
      "こんにちは！！"
]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)


#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)
chatterbotCorpusTrainer.train('chatterbot.corpus.english')




def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    return HttpResponse("list1")

#def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatReponse = str(bot.get_response(userMessage))
    return HttpResponse(chatReponse)

def chatbot_iframe(request):
    return render(request, 'blog/chat_iframe.html')

#openai
from django.http import HttpResponse
from openai import OpenAI
import os
import openai

# 環境変数からAPIキーを読み込む
# Renderに設定したキー名（例: OPENAI_API_KEY）と合わせる
openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key is None:
    raise ValueError("OPENAI_API_KEY 環境変数が設定されていません。")

# ... ChatGPT APIを呼び出すコード

from .models import ChatLog # 追加

client = OpenAI(api_key=openai.api_key)

def getResponse(request):
    user_message = request.GET.get('userMessage', '')
    
    if not user_message.strip():
        return HttpResponse("")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは親切な飲食店サポートチャットボットです。"},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message.content.strip()

        # ✅ チャットログを保存
        ChatLog.objects.create(user_message=user_message, bot_reply=reply)

        return HttpResponse(reply)

    except Exception as e:
        return HttpResponse(f"エラーが発生しました: {e}")
    
def history(request):
    logs = ChatLog.objects.order_by('-timestamp')[:20]
    return render(request, 'blog/history.html', {'logs': logs})
  

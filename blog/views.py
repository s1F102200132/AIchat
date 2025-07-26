from django.shortcuts import render
from django.http import HttpResponse
import openai
from django.http import HttpResponse

openai.api_key = 'AIzaSyCDH1Tm2II8ZhIkxSiUcEGj26UZ9f5KHOA'  # ここにキーを入れてください

def getResponse(request):
    user_message = request.GET.get('userMessage', '')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたは親切な飲食店サポートチャットボットです。"},
            {"role": "user", "content": user_message}
        ]
    )
    reply = response.choices[0].message.content.strip()
    return HttpResponse(reply)

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
chatterbotCorpusTrainer.train('chatterbot.corpus.spanish')



def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    return HttpResponse("list1")

def getResponse(request):
    user_message = request.GET.get('userMessage', '')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたは親切なアシスタントです。"},
            {"role": "user", "content": user_message}
        ]
    )
    reply = response['choices'][0]['message']['content'].strip()
    return HttpResponse(reply)

def chatbot_iframe(request):
    return render(request, 'blog/chat_iframe.html')


#gb
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
chatterbotCorpusTrainer.train('chatterbot.corpus.spanish')



def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    return HttpResponse("list1")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatReponse = str(bot.get_response(userMessage))
    return HttpResponse(chatReponse)

def chatbot_iframe(request):
    return render(request, 'blog/chat_iframe.html')

#jjjjjj

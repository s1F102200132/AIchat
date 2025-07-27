from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('specific', views.specific,name='specific'),
    
    path('getResponse',views.getResponse,name='getResponse'),
    
    path('chatbot/', views.chatbot_iframe, name='chatbot_iframe'),  # 追加
    
    path('history/', views.history, name='history')
] 
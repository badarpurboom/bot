from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time


chatbot = ChatBot("badarpur boom")
trainer = ListTrainer(chatbot)
trainer.train([
        "hi",
        "hi kya haal h ",
        "me thik hu ",
        "thanx "
        "your name ",
        "my name is Badarpur Boom AI bot "])

def msg(x):
    responce = chatbot.get_response(x)
    return responce


def home(request):

    return render(request,'home.html')

def about(request):
    text_t=request.GET.get('text')
    print(text_t)
    reply=msg(text_t)
    mapo={'bot':reply,'user':text_t}
    return render(request,'home.html',mapo)
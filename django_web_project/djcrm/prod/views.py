from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def a(request):
    return HttpResponse("i am a of prod")
    
def b(request):
    return HttpResponse ("i am b of prod")
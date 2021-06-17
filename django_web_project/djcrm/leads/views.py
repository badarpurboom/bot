from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def a(request):
    return HttpResponse("I am A page of leads")

def b(request):
    return HttpResponse("I am B page leads")
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home/home.html')

def book(request):
    return render(request,'home/book.html')
    
def about(request):
    return render(request,'home/about.html')
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('book/', views.book,name='book'),
    path('about/', views.about,name='about'),
    
]
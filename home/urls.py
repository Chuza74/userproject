from django.contrib import admin
from django.urls import path, include
from home import views
from . import views

urlpatterns = [ 
    path('',views.home, name="home"),
    path('home',views.home, name="home"),
    path('login',views.loginUser, name="login"),
    path('signup',views.regUser, name="signup"),
    path('logout',views.logoutUser, name="logout"),
    path('index',views.index, name="index"),
    path('about',views.about, name="about"),
    path('reg',views.reg, name="reg"),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]

from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('',views.index, name='index'),
    path('<str:name1>_<str:name2>/', views.room, name='room'),
]
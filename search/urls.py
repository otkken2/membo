from django.urls import path
from .import views
from django.views.decorators.cache import cache_page 


app_name = 'search'
urlpatterns = [
    path('',views.search,name='bosyuu_article')
]
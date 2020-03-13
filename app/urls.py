from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import cache_page 


app_name = 'app'
urlpatterns = [
    path('',cache_page(60*5)(views.index),name='index'),
    path('mypage',cache_page(60*1)(views.mypage), name='mypage'),
    path('createpost/',cache_page(60*1)(views.createpost), name='createpost'),
    path('bosyuu_detail<int:postcontent_id>/editpost/',views.editpost,name='bosyuu_edit'),
    path('bosyuu_detail<int:postcontent_id>/',cache_page(60*1)(views.bosyuu_detail), name='bosyuu_detail'),
    path('bosyuu_detail<int:postcontent_id>/delete/',views.bosyuu_delete,name='bosyuu_delete'),
    path('signup/', views.signup, name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='app/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


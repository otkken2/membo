from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'app'
urlpatterns = [
    path('',views.index,name='index'),
    path('mypage',views.mypage, name='mypage'),
    path('createpost/',views.createpost, name='createpost'),
    path('post_detail/bosyuu_detail',views.bosyuu_detail, name='bosyuu_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='app/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
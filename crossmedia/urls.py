from django.urls import path
from myApp import views

app_name = 'myApp'

urlpatterns = [
    path(r'', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('login/user_login',views.user_login,name='userlogin'),
]
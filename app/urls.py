from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.index, name='index'),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('processed', views.processed, name="processed"),
    path('userlogin', views.userlogin, name="userlogin"),
    path('logout/', views.logout, name="logout"),
    path('empdata', views.empdata, name="empdata")
]
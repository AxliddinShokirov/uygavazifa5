from django.urls import path
from Goods import views

urlpatterns = [
    path('login', views.login, name='login')
]
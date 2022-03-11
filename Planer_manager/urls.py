from django.urls import path

from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('', MainPage.as_view(), name="main_page"),
    path("planer", constructor, name='Planer-constructor'),


]


from django.urls import path
from book_shop.views import hello, MyPage

urlpatterns = [

    path('hello/', hello),
    path('', MyPage.as_view(), name='the-main-page')
]
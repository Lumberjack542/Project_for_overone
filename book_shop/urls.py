from django.urls import path
from book_shop.views import hello, MyPage

urlpatterns = [

    path('hello/', hello),
    path('books', MyPage.as_view(), name='book_page')
]
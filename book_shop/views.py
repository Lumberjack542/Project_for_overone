from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views import View

from book_shop.models import Book


def hello(request, name='vlad', digit=None):
    if digit is not None:
        return HttpResponse(f"is {digit}")
    return HttpResponse(f'hello {name}')


class MyPage(View):
    def get(self, request):
        context = {'books': Book.objects.all()}
        return render(request, 'book_shop/books.html', context)

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Planer
from .forms import PlanerForm
from django.contrib import messages
# Create your views here.


def constructor(request):
    if request.method == "POST":
        form = PlanerForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('main_page')

        else:
            error = 'error'

    form = PlanerForm()
    context = {
               "form": form}
    return render(request, "create_planer.html", context)


class MainPage(View):
    def get(self, request):
        context = {"element": Planer.objects.all()}
        return render(request, 'untitled.html', context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "registration completed successfully")
            return redirect('main_page')
        else:
            messages.error(request, 'Error')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {"form": form})


def login(request):
    return render(request, 'ligin.html')

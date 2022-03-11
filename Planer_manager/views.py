from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Planer
from .forms import PlanerForm, UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout
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
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "registration completed successfully")
            return redirect('main_page')
        else:
            messages.error(request, 'Error')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {"form": form})


def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page')
        else:
            form = UserLoginForm()

    return render(request, 'login.html', {'form': form})

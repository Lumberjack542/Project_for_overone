from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Planer, Comment
from django import forms


class PlanerForm(ModelForm):
    class Meta:
        model = Planer
        fields = ["title", "description", "image"]

        widgets = {
            'title': TextInput(attrs={
                "placeholder": "Название планера",
                'class': "form-control"
            }),

            "description": Textarea(attrs={
                "placeholder": "1.Утро - Действие\n2.Обед - Действие\n3.Ужин - Действие",
                'class': "form-control"
            }),

        }


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password1 = forms.CharField(max_length=50, label='Пароль', help_text='*Пароль должен содержать прописные и строчные буквы', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=50, label='Подтверждение пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
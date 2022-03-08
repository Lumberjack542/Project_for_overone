from django.forms import ModelForm, TextInput, Textarea

from .models import Planer, Comment


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
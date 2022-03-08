from django.contrib import admin
from .models import Planer, Comment
# Register your models here.


# class CommentAdmin(admin.StackedInline):
#     model = Comment
#     extra = 0
#
#
# class PlanerAdmin(admin.ModelAdmin):
#     inlines = [CommentAdmin]


admin.site.register(Planer)

from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from book_shop.models import Book, Comment
from book_shop.models import Comment, Mark


class CommentAdmin(admin.StackedInline):
    model = Comment
    extra = 0


class MarkAdmin(admin.StackedInline):
    model = Mark
    extra = 0


class BookAdmin(admin.ModelAdmin):
    inlines = [CommentAdmin, MarkAdmin]


admin.site.register(Book, BookAdmin)


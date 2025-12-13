from django.contrib import admin

from blog.models import Category, Article, Comment, Tag

# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Tag)
from django.contrib import admin
from blogapp.models import Category, Post, Tag
#
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)

# Register your models here.

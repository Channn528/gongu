from django.contrib import admin

from .models import Content, Tag, User
# Register your models here.
admin.site.register(Content)
admin.site.register(Tag)

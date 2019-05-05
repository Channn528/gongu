from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Content, Tag, User
# Register your models here.
admin.site.register(Content)
admin.site.register(Tag)

admin.site.register(User, UserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CategoryNews, News, CustomUser

# Register your models here.

admin.site.register(CategoryNews)
admin.site.register(News)
admin.site.register(CustomUser, UserAdmin)
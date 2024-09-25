from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'nick_name', 'birthday', 'tg_nick', 'vk_nick')
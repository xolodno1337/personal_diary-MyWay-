from django.contrib import admin
from diary.models import Diary


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'context', 'date_event', 'created_at', 'is_active', 'owner')

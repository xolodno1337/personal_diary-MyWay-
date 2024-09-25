from django.urls import path
from diary.apps import DiaryConfig
from diary.views import home

app_name = DiaryConfig.name

urlpatterns = [
    path('', home, name='home')
]

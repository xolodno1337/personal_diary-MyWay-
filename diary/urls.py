from django.urls import path
from diary.apps import DiaryConfig
from diary.views import base, DiaryListView, DiaryDetailView, DiaryCreateView, DiaryUpdateView, DiaryDeleteView, \
    DiaryPersonalListView

app_name = DiaryConfig.name

urlpatterns = [
    path('', base, name='base'),
    path('diary/', DiaryListView.as_view(), name='diary_list'),
    path('diary_personal/', DiaryPersonalListView.as_view(), name='diary_personal_list'),
    path('diary/create', DiaryCreateView.as_view(), name='diary_create'),
    path('diary/<int:pk>/', DiaryDetailView.as_view(), name='diary_detail'),
    path('diary/update/<int:pk>/', DiaryUpdateView.as_view(), name='diary_update'),
    path('diary/delete/<int:pk>/', DiaryDeleteView.as_view(), name='diary_delete'),
]

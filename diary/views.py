from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from diary.models import Diary


def base(request):
    return render(request, 'base.html')


class DiaryListView(ListView):
    model = Diary
    template_name = 'diary/diary_list.html'


class DiaryDetailView(DetailView):
    model = Diary
    template_name = 'diary/diary_detail.html'


class DiaryCreateView(CreateView):
    model = Diary
    fields = ('title', 'image', 'context', 'date_event', 'is_active')
    success_url = reverse_lazy('diary:diary_list')


class DiaryUpdateView(UpdateView):
    model = Diary
    fields = ('title', 'image', 'context', 'date_event', 'is_active')
    success_url = reverse_lazy('diary:diary_list')


class DiaryDeleteView(DeleteView):
    model = Diary
    success_url = reverse_lazy('diary:diary_list')

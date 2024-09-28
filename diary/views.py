from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from diary.forms import DiaryUpdateForm
from diary.models import Diary


def base(request):
    return render(request, 'base.html')


class DiaryListView(LoginRequiredMixin, ListView):
    model = Diary
    template_name = 'diary/diary_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Diary.objects.all().order_by('-created_at')
        else:
            return Diary.objects.filter(is_active=True).order_by('-created_at')


class DiaryDetailView(LoginRequiredMixin, DetailView):
    model = Diary
    template_name = 'diary/diary_detail.html'


class DiaryCreateView(CreateView):
    model = Diary
    fields = ('title', 'image', 'context', 'date_event', 'is_active')
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save()
        user = self.request.user
        diary.owner = user
        diary.save()
        return super().form_valid(form)


class DiaryUpdateView(LoginRequiredMixin, UpdateView):
    model = Diary
    form_class = DiaryUpdateForm
    success_url = reverse_lazy('diary:diary_list')

    def get_queryset(self):
        return Diary.objects.filter(owner=self.request.user)


class DiaryDeleteView(LoginRequiredMixin, DeleteView):
    model = Diary
    success_url = reverse_lazy('diary:diary_list')


class DiaryPersonalListView(LoginRequiredMixin, ListView):
    model = Diary
    template_name = 'diary/diary_personal_list.html'

    def get_queryset(self):
        return Diary.objects.filter(owner=self.request.user).order_by('-created_at')

import secrets
import string
import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject='Подтверждение почты',
            message=f'Для подтверждения вашей почты перейдите по ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserListView(LoginRequiredMixin, ListView):
    model = User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('nick_name', 'avatar', 'birthday', 'phone', 'tg_nick', 'vk_nick')
    success_url = reverse_lazy('diary:diary_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_editing'] = True
        return context


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('diary:base')


def reset_password(request):
    context = {
        'success_message': 'Пароль успешно сброшен. Новый пароль был отправлен на адрес Вашей электронной почты.',
    }

    if request.method == 'POST':
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        characters = string.ascii_letters + string.digits
        characters_list = list(characters)
        random.shuffle(characters_list)
        password = ''.join(characters_list[:10])
        user.set_password(password)
        user.save()

        send_mail(
            subject='Восстановление пароля',
            message=f'Ваш пароль для доступа на наш сайт изменен:\n {password}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return render(request, 'base.html', context)
    return render(request, 'users/reset_password.html')

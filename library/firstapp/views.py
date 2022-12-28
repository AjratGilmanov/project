from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import Application
from .forms import *
from .models import Book


class Index(ListView):
    model = Book
    template_name = 'firstapp/index.html'


    # def get_queryset(self):
    #     pass

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Books'] = Book.objects.all()
        return context


class Form(CreateView):
    form_class = Application
    template_name = 'firstapp/form.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, form=form_class, **kwargs):
        return {'form': form}


class Reg(CreateView):
    form_class = RegistrFrom # Django форма для регистрации

    template_name = 'firstapp/reg.html' # ссылка на шаблон (где хранится это html)
    success_url = reverse_lazy('login') # В случае успешной регистрации пользователя перенаправлет туда

    def get_context_data(self, form=form_class, **kwargs):
        return {'form': form}

    # def post(self, request, *args, **kwargs):
    #     pass

class Log(LoginView):
    form_class = Entrance
    template_name = 'firstapp/log.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, form=form_class, **kwargs):
        return {'form': form}


def Logout_user(request):
    logout(request)
    return redirect('home')





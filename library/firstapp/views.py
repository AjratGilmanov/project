from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponseRedirect

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView

from .forms import Application
from .forms import *
from .models import Book, Category, Author


class Index(ListView):
    model = Book
    template_name = 'firstapp/index.html'




    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Books'] = Book.objects.all()
        return context


class Form(CreateView):
    form_class = Application
    template_name = 'firstapp/form.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, form=form_class, **kwargs):
        intilizer()
        return {'form': form}

class Edit(UpdateView):
    model = Book
    template_name_suffix = 'edit'
    success_url = reverse_lazy('home')
    form_class = Application

    def get_context_data(self, form=form_class, **kwargs):
        intilizer()
        book_obj = self.object
        form = form(initial={'book_name': book_obj.book_name,
                             'category': book_obj.category.all(),
                             'book_author': book_obj.book_author_id,
                             'date_of_create': book_obj.date_of_create
                              })
        return {'form': form}


def delete(request, id):
    try:
        cart = Book.objects.get(id=id)
    except:
        return HttpResponseNotFound('<h2>Person not found</h2>')
    cart.delete()
    return HttpResponseRedirect(reverse('home'))


class Reg(CreateView):
    form_class = RegistrFrom # Django форма для регистрации

    template_name = 'firstapp/reg.html' # ссылка на шаблон (где хранится это html)
    success_url = reverse_lazy('login') # В случае успешной регистрации пользователя перенаправлет туда

    def get_context_data(self, form=form_class, **kwargs):
        return {'form': form}

class Log(LoginView):
    form_class = Entrance
    template_name = 'firstapp/log.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, form=form_class, **kwargs):
        return {'form': form}


def Logout_user(request):
    logout(request)
    return redirect('home')

def intilizer():
    if Category.objects.all().count() == 0:
        Category.objects.create(name='Хоррор')
        Category.objects.create(name='Драма')
        Category.objects.create(name='Трилер')
    if Author.objects.all().count() == 0:
        Author.objects.create(name='Пушкин')
        Author.objects.create(name='Лермонтов')
        Author.objects.create(name='Толстой')



from django.shortcuts import render
from django.views.generic import CreateView

from django.urls import reverse_lazy           # получает URL по параметрам функции path()

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm                     # из какого класса взять форму
    success_url = reverse_lazy('posts:index')             # куда перенаправить в случае успешной отправки формы
    template_name = 'users/signup.html'          # шаблон, куда будет передана переменная form с объектом html-формы

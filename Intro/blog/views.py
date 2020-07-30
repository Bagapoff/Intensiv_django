
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World! <a href="/contacts">Контакты</a>')

def contacts(request):
    return HttpResponse('Email:123345.ru <a href="/">Назад</a>')
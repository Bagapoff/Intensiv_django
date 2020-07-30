
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Главная страница</h1><br> Hello world!<br> '
                        '<a href="/contacts">Контакты</a>  '
                        '<a href="/customers">Покупатели</a>')

def contacts(request):
    return HttpResponse('<h1>Контакты</h1>'
                        'Email:123345.ru<br>'
                        'Тел. 88005553535<br>'
                        '<a href="/">Главная</a>  '
                        '<a href="/customers">Покупатели</a>')

def customers(request):
    return HttpResponse('<h1>Покупатели</h1>'
                        'Ivan<br>'
                        'Petr<br>'
                        'Andrej<br> <a href="/">Главная</a>  '
                        '<a href="/contacts">Контакты</a>')
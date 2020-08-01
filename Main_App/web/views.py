import datetime
from django.shortcuts import render, redirect
from django.conf import settings

def index(request):
    return render(request, 'index.html')

messages_data = []

def contacts(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        email = request.POST.get('email', '')
        if (not email or not text):
            return render(request, 'contacts.html', {'error': 'Есть пустые поля'})

        mes = {
        'date': datetime.datetime.now(),
        'text': text,
        'email': email
        }
        f = open('messages.txt', 'a')

        f.write(str(mes['date'])+ '\n' +
                  str(mes['text']) + '\n' +
                  str(mes['email'])+ '\n \n \n')
        messages_data.append(mes)

    return render(request, 'contacts.html',context={
        'phone': '+8 800 555 35 35',
        'email': 'wassup@gmail.com',
    })

def publications (request):
    return render(request, 'publications.html', context={
        'publications': reversed(publications_data)
    })

publications_data = [
{       'id': 0,
        'title':'Публикация 0',
        'date': datetime.datetime.now(),
        'text': 'Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. <br>'
                '<i>Lorem Ipsum</i> используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации "Здесь ваш текст.. Здесь ваш текст.. Здесь ваш текст.." Многие программы электронной вёрстки и редакторы HTML используют Lorem Ipsum в качестве текста по умолчанию, так что поиск по ключевым словам "lorem ipsum" сразу показывает, как много веб-страниц всё ещё дожидаются своего настоящего рождения. За прошедшие годы текст Lorem Ipsum получил много версий. Некоторые версии появились по ошибке, некоторые - намеренно (например, юмористические варианты).'
},

{       'id': 1,
        'title':'Публикация 1',
        'date': datetime.datetime.now(),
        'text': 'За столом сидели, мужики и ели<br>'
                'Мясом конюх угощал своих гостей.<br>'
                'Все расхваливали ужин и хозяин весел был,<br>'
                'О жене своей все время говорил.<br>'
                'Ели мясо мужики, пивом запивали!<br>'
                'О чем конюх говорил, они не понимали!<br>'
                'Я узнал недавно, все вы, как ни странно,<br>'
                'Конюх хриплым голосом проговорил,<br>'
                'С моей бабою встречались в тайне от меня<br>'
                'И поэтому всех вас собрал сегодня Я!<br>'
},

{
        'id': 2,
        'title':'Публикация 2',
        'date': datetime.datetime.now(),
        'text': 'Третьего дня, по совету проверенных камрадов, приобрёл новый мегадевайс — «Сталин-3000». '
                'Сразу же, задыхаясь от жадности, вскрыл коробку цепкими лапами и заюзал мегадевайс. '
                'Размер, моё почтение. Настоящей глыбой был Иосиф Виссарионович.'

}
]

def publication(request, number):
    if number>len(publications_data):
        return redirect('/publications')
    return render(request, 'publication.html', context=publications_data[number])

def publish(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        text = request.POST.get('text', '')
        password = request.POST.get('pass', '')
        if (not title or not text or not password):
            return render(request, 'publish.html', {'error': 'Есть пустые поля'})
        if password != settings.PUBLISH_PASSWORD:
            return render(request, 'publish.html', {'error': 'Неверный пароль'})
        publications_data.append({
            'id':len(publications_data),
            'title':title,
            'date': datetime.datetime.now(),
            'text':text
        })
        return redirect('/publications/'+  str(publications_data[-1]['id']))

    return render(request, 'publish.html')

def messages (request):
    if len(messages_data) == 0:
        return render (request, 'messages.html', {'alert': 'Сообщений нет'})

    return render(request, 'messages.html', context={
        'messages': reversed(messages_data)
    })
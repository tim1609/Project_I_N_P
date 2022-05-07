from django.shortcuts import render



title = 'Тортуга Нашего времени'



def index(request):
    context = {'title': title,
               'text': 'Главная Страница',
               "names":["Рома", "Коля", "Вася", "Петя", "Маша"],
               }
    template = 'posts/index.html'
    return render(request, template, context)

def group_posts(request):
    template = 'posts/group_list.html'
    return render(request, template)

def spiski (request):
    context = {"names":["Рома", "Коля", "Вася", "Петя", "Маша"],}

    template = 'posts/spiski.html'
    return render(request, template, context)
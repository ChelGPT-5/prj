from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict[str, str] = {
        'title': "Главная",
        'content': "Грузоперевозки"
    }

    return render(request, 'main/index.html', context)


def about(request):
    context: dict[str, str] = {
        'title': "О нас",
        'content': "О нас",
        'text_on_page': "Добро пожаловать в мир грузоперевозок – вашего надежного партнера в сфере грузоперевозок."
    }

    return render(request, 'main/about.html', context)


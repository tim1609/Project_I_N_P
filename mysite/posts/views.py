from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse(
     ' <!DOCTYPE html>'
     '<html>'
     '<head>'
     '<meta charset="utf-8">'
     '<meta name="description" content="Моя авто-биография">'
     '<title>Авто-биография</title>'
     '<link rel="icon" href="https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/avatars/41/41fec79467434dc04b84b3c9460f58ee02da9709_medium.jpg" type="image">'
     '<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">'
     '<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">'
     '<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">'
     '<link rel="manifest" href="/site.webmanifest">'
     '<meta name="msapplication-TileColor" content="#da532c">'
     '<meta name="theme-color" content="#ffffff">'
     '</head>'
     '<body>'
     '<!-- заголовки -->'
     '<h1> Биография Рублёва Тимофея Ивановича </h1>'
     '<! -- ранние периоды жизни -->'
     '<p> Я родился в <a href=https://armius.ru/rvsn/vch52015 > Комсомольск-на-Амуре-31 </a> 16.09.2007, где прожил 12 лет. </p>'
     '<p> Там я учился в школе №140 (школа преписанная к воинской части), позже учился в г.Краснодаре, <a href=https://school48suvorov.ru/ > в лицее №48 имени А.В. Суворова </a>. </p>'
     '<p> Год я проучился в "инжинерном" классе, и переехал в г.Сочи. В Сочи по мимо учёбы в школе №28, я начал заниматься програмированием. </p>'
     '<!-- програмирование -->'
     '<p> Начал я с курса "Unity" на базе <a href=https://sochisirius.ru/ > Сириуса </a> , после его завершения я занялся языком програмирования "Python", первый год я проучился под руководством Соловова М.А., а второй под руководством Перекальского И.Н.. </p>'
     '<!-- ссылки -->'
     '<p> <a href=https://vk.com/tim1609 > ВКонтакте </a> , <a href=https://discord.gg/ANvFjhfxNx > Discord </a>   '
     '</body>'
     '</html>'
           )





def group_posts(request):
    return HttpResponse('Главная страница')


from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse(
     '<!DOCTYPE html>'
     ' <html>'
     ' <head>'
     ' <meta charset="utf-8">'
     '<meta name="description" content="Краткое описание страницы">'
     '<title>Тортуга нашего времени</title>'
     '<link rel="icon" href="http://2.bp.blogspot.com/-gSoC3dc2HpE/VeQKtTTh4XI/AAAAAAAAJsw/3qnbEwMWHzs/s1600/13756508429489.jpg" type="image">'
     '<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">'
     '<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">'
     '<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">'
     '<link rel="manifest" href="http://2.bp.blogspot.com/-gSoC3dc2HpE/VeQKtTTh4XI/AAAAAAAAJsw/3qnbEwMWHzs/s1600/13756508429489.jpg ">'
     '<meta name="msapplication-TileColor" content="#da532c">'
     '<meta name="theme-color" content="#ffffff">'
     '</head>'
     '<body>'
     '<!-- Name -->'
     '<h1> Тимофей </h1>'
     '<!-- Surname -->'
     '<h2> Сода </h2>'
     '<!-- Idk -->'
     '<h3> Иванович </h3>'
     '<!-- Text -->'
     '<p> Текст </p>'
     '<p>  <i> Красивый текст </i>'
     '<p>  <b> Жирный текст </b>  </p>'
     '<!-- Cs -->'
     '<p>  <a href=https://play-cs.com/ru/ >'
     'CS '
     '</a>  </p>'
     '<!-- Image -->'
     '<img width="800px" height="500px" src=http://2.bp.blogspot.com/-gSoC3dc2HpE/VeQKtTTh4XI/AAAAAAAAJsw/3qnbEwMWHzs/s1600/13756508429489.jpg >'
     '<!-- Language -->'
     '<p> Языки програмирования'
     '<ul>'
     '<li>Python</li>'
     '<li>HTML</li>'
     '<li>C++</li>'
     '<li>JaVa</li>'
     '</ul>  </p>'
     '<!-- Firend -->'
     '<p> Друзья'
     '<ol> '
     '<li>1</li>'
     '<li>1</li>'
     '<li>1</li>'
     '<li>1</li>'
     '</ol>  </p>'
     '</body>'
     '</html> ')




def group_posts(request):
    return HttpResponse('Главная страница')


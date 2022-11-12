from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

def index(request):
    return HttpResponse("Страница приложения women.")

def categories(request, cat_id):
    if(request.POST):
        print(request.POST)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat_id}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', parmanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

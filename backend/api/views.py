from django.shortcuts import render
from django.http import JsonResponse

import json
import requests
from bs4 import BeautifulSoup

def search(request, keyword):
    r = requests.get(f'https://search.daum.net/search?w=news&q={keyword}')
    soup = BeautifulSoup(r.text, 'html.parser')
    tags = soup.select('ul#clusterResultUL > li')
    articles = []
    for tag in tags:
        nb = tag.select_one('a.f_nb')
        if nb == None:
            continue
        articles.append({
            'title': tag.select_one('a.f_link_b').text,
            'url': tag.select_one('a.f_nb')['href'],
            'desc': tag.select_one('p.desc').text
        })
    return JsonResponse({'list':articles})

def register(request):
    data = json.loads(request.body.decode('utf-8'))
    #data.title
    return JsonResponse(data)



from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

import json
import requests
from bs4 import BeautifulSoup

from api.models import Article

import logging
logger = logging.getLogger('django')

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
    ## STEP 1
    data = json.loads(request.body)
    url = data['url']
    title = data['title']
    desc = data['desc']
    pub_date = timezone.now()
    articles = Article.objects.filter(url=url) 
    if articles.exists():
        a = articles.first()
        a.url = url
        a.title = title
        a.desc = desc
        a.pub_date = pub_date
    else:
        a = Article(url=url, title=title, desc=desc, pub_date=pub_date)
    a.save()

    ## STEP 2
    # r = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    # soup = BeautifulSoup(r.text, 'html.parser')

    # title = soup.find("meta", property="og:title")
    # title = title["content"] if title else None

    # content = soup.select_one('#harmonyContainer section')
    # content = "".join([str(x) for x in content.contents])
    # content = content.strip()
    

    return JsonResponse(data)



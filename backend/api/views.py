from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

import json
import requests
from bs4 import BeautifulSoup
import os

from api.models import Article
from google_trans_new import google_translator
from textblob import TextBlob

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

def articles(request):
    data = list(Article.objects.values().order_by('-pub_date'))
    return JsonResponse(data, safe=False)  

def polars(request):
    data = list(Article.objects.values().order_by('-avg_polarity'))
    return JsonResponse(data, safe=False)  

def register(request):
    ## STEP 1
    data = json.loads(request.body)
    url = data['url']
    title = data['title']
    desc = data['desc']
    pub_date = timezone.now()
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0]

    articles = Article.objects.filter(url=url) 
    if articles.exists():
        a = articles.first()
    else:
        a = Article()

    a.url = url
    a.title = title
    a.desc = desc
    a.user_ip = user_ip
    a.pub_date = pub_date
    
    ## STEP 2
    translator = google_translator()

    r = requests.get('http://'+os.environ['DJANGO_BROWSER_SERVER']+'/browser/get.php?url='+url)
    j = json.loads(r.text)
    page = j['page']
    #logger.info(page)
    soup = BeautifulSoup(page, 'html.parser')

    title = soup.find("meta", property="og:title")
    title = title["content"] if title else None

    content = soup.select_one('#harmonyContainer section')
    #content = "".join([str(x) for x in content.contents])
    content = content.get_text().strip()
    
    tags = soup.select('ul.list_comment > li p.desc_txt')
    comments = []
    polarities = []
    for tag in tags:
        comment = tag.contents[0]
        comments.append(comment)
        en = translator.translate(comment, lang_tgt='en')
        logger.info(en)
        blob = TextBlob(en)
        sentence_polarities = []
        for sentence in blob.sentences:
            sentence_polarities.append(sentence.sentiment.polarity)
        if len(sentence_polarities) < 1:
            polarity = 0
        else: 
            polarity = sum(sentence_polarities)/len(sentence_polarities)
        polarities.append(polarity)
    comments_count = len(comments)
    if comments_count > 0:
        avg_polarity = sum(polarities)/comments_count
    else:
        avg_polarity = 0

    a.title = title
    a.content = content
    a.comments = "||||".join(comments)
    a.comments_count = comments_count
    a.polarities = "||||".join(map(str,polarities))
    a.avg_polarity = avg_polarity
    a.save()

    return JsonResponse({'msg':'ok'})



from django.urls import path
from api import views

urlpatterns = [
    path('search/<str:keyword>', views.search),
    path('register', views.register),
    path('articles', views.articles),
    path('polars', views.polars),
]

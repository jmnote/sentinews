from django.urls import path
from api import views

urlpatterns = [
    path('search/<str:keyword>', views.search),
]

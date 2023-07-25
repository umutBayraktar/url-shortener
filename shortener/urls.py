from django.contrib import admin
from django.urls import path, include
from shortener.views import HashURLAPIView, RedirectToHashedURL

app_name = 'shortener'

urlpatterns = [
     path('',HashURLAPIView.as_view(), name='hash_url_api'),
     path('<str:hashed_url>/', RedirectToHashedURL.as_view(), name='redirect_to_hashed_url'),
]

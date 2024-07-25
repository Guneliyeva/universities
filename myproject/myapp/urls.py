from django.urls import path
from .views import search_universities

urlpatterns = [
    path('', search_universities, name='search_universities'),
]

from django.urls import path
from .views import num_to_english_get, num_to_english_post

urlpatterns = [
    path('num_to_english', num_to_english_get, name='num_to_english_get'),
    path('num_to_english', num_to_english_post, name='num_to_english_post'),
]

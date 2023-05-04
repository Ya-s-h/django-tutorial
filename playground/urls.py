# Similar to router in Express

from django.urls import path
from . import views

# URL Configuration
urlpatterns = [
    path('hello/', views.say_hello) # Always end route with /
]

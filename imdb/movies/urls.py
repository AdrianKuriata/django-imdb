from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.show, name='show'),
    path('genres/<slug:slug>/', views.genre, name='genre')
]

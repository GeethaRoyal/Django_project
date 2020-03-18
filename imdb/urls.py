from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:movie_id>/', views.movie, name='movie'),
    path('actor/<int:actor_id>/', views.actor, name='actor'),
    path('director/<int:director_id>/', views.director, name='director'),
    path('analytics/', views.analytics, name='analytics'),
]

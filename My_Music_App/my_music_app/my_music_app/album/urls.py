from django.contrib import admin
from django.urls import path, include

from my_music_app.album import views

urlpatterns = [
    path('add/', views.add_album, name='add album page'),
    path('details/<pk>/', views.details_album, name='album details page'),
    path('edit/<pk>/', views.edit_album, name='edit album page'),
    path('delete/<pk>/', views.delete_album, name='delete album page')
]

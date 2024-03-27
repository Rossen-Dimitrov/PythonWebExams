
from django.urls import path
from my_music_app.user_profile import views

urlpatterns = [
    path('add/', views.add_profile, name='add profile'),
    path('details/', views.details_profile, name='details profile'),
    path('delete/', views.delete_profile, name='delete profile'),
]

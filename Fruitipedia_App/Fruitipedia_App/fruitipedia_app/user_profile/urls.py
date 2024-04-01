from django.urls import path
from fruitipedia_app.user_profile import views

urlpatterns = [
    path('create/', views.create_profile, name='profile create page'),
    path('details/', views.profile_details, name='profile details page'),
    path('edit/', views.edit_profile, name='profile edit page'),
    path('delete/', views.delete_profile, name='profile delete page'),
]

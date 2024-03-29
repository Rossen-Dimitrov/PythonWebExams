from django.urls import path

from expenses_tracker.user_profile import views

urlpatterns = [

    path('', views.details_profile, name='profile details'),
    path('add/', views.add_profile, name='profile add page'),
    path('edit/', views.edit_profile, name='profile edit page'),
    path('delete/', views.delete_profile, name='profile delete page'),
]


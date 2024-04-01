
from django.urls import path, include
from fruitipedia_app.core import views as core_views
from fruitipedia_app.fruit import views

urlpatterns = [
    path('create/', views.create_fruit, name='fruit create page'),
    path('<fruitId>/details/', views.details_fruit, name='fruit details page'),
    path('<fruitId>/edit/', views.edit_fruit, name='fruit edit page'),
    path('<fruitId>/delete/', views.delete_fruit, name='fruit delete page'),
]



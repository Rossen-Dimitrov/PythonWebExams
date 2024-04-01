from django.contrib import admin
from django.urls import path, include
from fruitipedia_app.core import views as core_views
from fruitipedia_app.fruit import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name='index page'),
    path('profile/', include('fruitipedia_app.user_profile.urls')),
    path('dashboard/', core_views.dashboard, name='dashboard page'),
    path('create/', views.create_fruit, name='fruit create page'),
    path('fruite/', include('fruitipedia_app.fruit.urls')),
]



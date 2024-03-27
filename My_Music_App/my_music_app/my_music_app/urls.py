from django.contrib import admin
from django.urls import path, include

from my_music_app.common import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home page'),
    path('album/', include('my_music_app.album.urls')),
    path('profile/', include('my_music_app.user_profile.urls')),

]

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from expenses_tracker.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home page'),
    path('expense/',  include('expenses_tracker.expense.urls')),
    path('profile/',  include('expenses_tracker.user_profile.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

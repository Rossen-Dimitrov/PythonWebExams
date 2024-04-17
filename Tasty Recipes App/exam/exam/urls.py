from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from exam import settings
from exam.core.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('recipe/', include('exam.recipe.urls')),
    path('profile/', include('exam.app_profile.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

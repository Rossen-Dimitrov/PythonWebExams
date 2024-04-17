from django.urls import path, include

from exam.app_profile.views import ProfileCreatView, ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('create/', ProfileCreatView.as_view(), name='profile create page'),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details page'),
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='profile edit page'),
    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile delete page'),
]




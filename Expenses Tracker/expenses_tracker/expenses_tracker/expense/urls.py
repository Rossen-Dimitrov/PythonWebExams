from django.urls import path, include

from expenses_tracker.expense import views

urlpatterns = [
    path('create/', views.create_expense, name="expense create page"),
    path('edit/<pk>/', views.edit_expense, name="expense edit page"),
    path('delete/<pk>/', views.delete_expense, name="expense delete page"),
]

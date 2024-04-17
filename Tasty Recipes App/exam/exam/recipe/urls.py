from django.urls import path, include
from exam.recipe.views import CatalogListView, RecipeCreatView, RecipeDetailsView, RecipeEditView, RecipeDeleteView

urlpatterns = [
    path('catalogue/', CatalogListView.as_view(), name='catalogue'),
    path('create/', RecipeCreatView.as_view(), name='recipe create page'),
    path('<int:pk>/', include([
        path('details/', RecipeDetailsView.as_view(), name='recipe details page'),
        path('edit/', RecipeEditView.as_view(), name='recipe edit page'),
        path('delete/', RecipeDeleteView.as_view(), name='recipe delete page'),
    ])),
]

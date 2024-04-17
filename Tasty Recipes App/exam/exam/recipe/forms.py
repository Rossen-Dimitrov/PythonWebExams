from django import forms

from exam.recipe.models import Recipe


class RecipeCreatForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']

        widgets = {
            'ingredients': forms.Textarea(attrs={'placeholder': 'ingredient1, ingredient2, ...'}),
            'instructions': forms.Textarea(attrs={'placeholder': 'Enter detailed instructions here...'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Optional image URL here...'}),
            'cooking_time': forms.NumberInput(attrs={'placeholder': 'Cooking  Ttime'}),
        }
        labels = {
            'cuisine_type': 'Cuisine Type',
            'cooking_time': 'Cooking Time',
            'image_url': 'Image URL',
        }

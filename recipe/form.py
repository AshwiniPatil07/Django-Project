from django import forms
# importing attribute to add them to form
from recipe.models import Recipe

class RecipeForm(forms.ModelForm):

    class Meta:
        model=Recipe
        fields='__all__'
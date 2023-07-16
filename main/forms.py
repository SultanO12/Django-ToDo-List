from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title", 'description', 'priority', 'completed', 'category')

class CategoruForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name", "slug", "favorite", "archived")
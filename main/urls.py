from django.urls import path
from .views import index, categories, add_form, delete_task, update_task, done_task, add_catigory

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('category/<slug:slug>', categories.as_view(), name='categories'),
    path('add_task/', add_form.as_view(), name="add_form"),
    path('add_category/', add_catigory.as_view(), name="add_category"),
    path('delete-task/<int:id>', delete_task.as_view(), name="delete_task"),
    path('update-task/<int:id>', update_task.as_view(), name="update_task"),
    path('done-task/<int:id>', done_task.as_view(), name="done_task")
]
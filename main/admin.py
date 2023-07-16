from django.contrib import admin
from .models import Category, Task

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'favorite', 'archived']
    fields = ['name', 'slug', 'favorite', 'archived', 'created', 'updated']
    prepopulated_fields = {"slug": ("name", )}
    search_fields = ['name', 'archived']
    readonly_fields = ['created', 'updated']
    list_filter = ['created', 'updated']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "priority", 'completed', "category", 'created', 'updated')
    fields = ("title", 'description', "priority", 'completed', "category")
    readonly_fields = ['created', 'updated']
    search_fields = ("title", "priority", 'completed', "category")
    list_filter = ['created', 'updated']

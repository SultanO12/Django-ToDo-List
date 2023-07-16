from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Category, Task
from .forms import TaskForm, CategoruForm


class index(View):
    def get(self, request, *args, **kwargs):
        cats = Category.objects.all()
        tasks = Task.objects.all()
        return render(request, "main/index.html", {"tasks":tasks, "cats":cats})
    

class categories(View):
    def get(self, request, slug, *args, **kwargs):
        cats = Category.objects.all()
        task = Category.objects.get(slug=slug)
        tasks = task.tasks.all()
        category_name = task.name
        return render(request, 'main/cat_task.html', {"tasks":tasks, "cats":cats, "category_name":category_name})

class add_form(View):
    def get(self, request, *args, **kwargs):
        cats = Category.objects.all()
        form = TaskForm()
        return render(request, "main/add_task.html", context={"form":form, "cats":cats})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

class add_catigory(View):
    def get(self, request, *args, **kwargs):
        cats = Category.objects.all()
        form = CategoruForm()
        return render(request, "main/add_category.html", context={"form":form, "cats":cats})

    def post(self, request):
        form = CategoruForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
          
class update_task(View):
    def get(self, request, id, *args, **kwargs):
        cats = Category.objects.all()
        task = get_object_or_404(Task, id=id)
        form = TaskForm(instance=task)
        return render(request, "main/update_task.html", context={"form":form, "cats":cats})

    def post(self, request, id):
        task = get_object_or_404(Task, id=id)
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


class delete_task(View):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        task.delete()
        return redirect('index')

class done_task(View):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        if task.completed == False:
            task.completed = True
        else:
            task.completed = False
        task.save()
        return redirect('index')
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    favorite = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
class Task(models.Model):
    priorit = (
        ("H", "High"),
        ("M", "Middle"),
        ("L", "Low")
    )

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(choices=priorit)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="tasks")

    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta: 
        ordering = ["completed", "priority"]
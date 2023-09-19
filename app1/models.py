from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=220,unique=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.task
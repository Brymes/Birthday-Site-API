from django.db import models

# Create your models here.

class Wishes(models.Model):
    
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=30, default="Anonymous")
    message = models.TextField(blank=False, null=True, help_text="Birthday Message")
from django.db import models

# Create your models here.
class Books(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=40)
    published_date=models.DateField()
    desc=models.TextField()
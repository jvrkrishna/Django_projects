from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    img=models.ImageField(upload_to='Images/')
    author=models.CharField(max_length=50)
    created_at=models.DateTimeField(default=datetime.now)
    is_published=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
from django.db import models

class Sample(models.Model):
    # Fields of the model
    title = models.CharField(max_length=100)
    description = models.TextField()
    author=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Optional: String representation of the object
    def __str__(self):
        return self.title
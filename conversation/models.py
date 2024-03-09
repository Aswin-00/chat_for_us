from django.db import models

# Create your models here.

class chat_data(models.Model):
    CONTENT_CHOICES = [
        ('she', 'she'),
        ('me', 'me'),
        
    ]
     
    content=models.CharField(max_length=100)
    # name=models.CharField(max_length=40)
    name = models.CharField(max_length=40, choices=CONTENT_CHOICES)

    data=models.DateTimeField(auto_now_add=True)

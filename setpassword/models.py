from django.db import models
# Create your models here.
class Token(models.Model):
    email = models.CharField(max_length=50)
    token = models.CharField(max_length=100)
    expired = models.CharField(max_length=50)
    
    def __str__(self):
        return self.email
from django.db import models
# Create your models here.
class Data(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    photo = models.CharField(max_length=200,null=True)
    template = models.IntegerField(null=True)
    color = models.TextField(null=True)
    description = models.TextField(null=True)
    website = models.CharField(max_length=100,null=True)
    address = models.TextField(null=True)
    telp = models.IntegerField(null=True)
    social = models.TextField(null=True)
    education = models.TextField(null=True)
    vision = models.TextField(null=True)
    skill = models.TextField(null=True)
    achievement = models.TextField(null=True)
    experience = models.TextField(null=True)
    
    def __str__(self):
        return self.user
    

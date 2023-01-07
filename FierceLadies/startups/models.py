from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class startupModel(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.SET_NULL)
    logo = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=50,unique=True,null=False,blank=False)
    description = models.TextField(max_length=500,null=True,blank=True)
    founded = models.IntegerField(null=False,blank=False)
    location = models.CharField(max_length=100,null=False,blank=False)
    website = models.URLField(max_length=50,null=True,blank=True)

    def save(self,*args):
        self.user = User.objects.filter(user)
        super().save(self)

    def __str__(self):
        return self.name
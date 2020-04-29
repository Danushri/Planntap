from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Diary(models.Model):
    member = models.ForeignKey(User,on_delete=models.CASCADE) #one user can post multiple diary entries
    Eventname = models.CharField(max_length=200)
    desc = models.TextField(max_length = 2000, null=True)
    Location = models.CharField(max_length=200, null=True)
    Date = models.DateField(null=True)
    Image = models.ImageField(upload_to = 'static/Mainapp/images', default = 'static/Mainapp/images/sakura.jpg') #specify size later
    Rating = models.PositiveIntegerField(null=True)
    Review = models.TextField(max_length = 2000, null=True)


    def __str__(self):
        return self.Eventname

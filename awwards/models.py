from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from .models import Category,Tags
from django_countries.fields import CountryField
from django.utils import timezone



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_image',default='https://res.cloudinary.com/dvhid4k2j/image/upload/v1654654901/png_rxb8cy.jpg')
    bio = models.CharField(max_length=150,blank=True)


    def __str__(self) -> str:
        return f'{self.user.username}'

class Category(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self) -> str:
        return f'{self.name}'

    

class Tags(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self) -> str:
        return f'{self.name}'

    


class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sitename = models.CharField(max_length=100)
    url = models.URLField(max_length=150)
    description = models.TextField()
    image = CloudinaryField('image',null=True)
    categories = models.ManyToManyField(Category,related_name='categories')
    tags = models.ManyToManyField(Tags,related_name='tags') 
    Technologies = models.TextField(null=True,blank=True)
    # designer details
    designer_name = models.CharField(max_length=100)
    designer_url = models.URLField(max_length=150)
    date_submited = models.DateTimeField(default=timezone.now)
    rank = models.BigIntegerField(null=True,blank=True) 
    country = CountryField()



    def __str__(self) -> str:
        return f'{self.sitename}'

    

class Vote(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    average_score = models.DecimalField(max_digits=2,decimal_places=2)


    def __str__(self) -> str:
        return f'{self.user.username}'

    


    





    

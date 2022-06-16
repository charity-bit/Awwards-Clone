from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from .models import Category,Tags
from django_countries.fields import CountryField
from django.utils import timezone

from random import randint

DESIGN_CHOICES = zip(range(1,11), range(1,11))
USABILITY_CHOICES = zip(range(1,11), range(1,11))
CONTENT_CHOICES = zip(range(1,11), range(1,11))
profile_pics = [
    'https://res.cloudinary.com/dvhid4k2j/image/upload/v1655073458/px6e6mggnblfxey90w3j.jpg',
    'https://res.cloudinary.com/dvhid4k2j/image/upload/v1655419775/Snapchat-667489474_tywlo1.jpg',
    'https://res.cloudinary.com/dvhid4k2j/image/upload/v1655419777/1-10012_kitten-cute-cats-orange-tabby-cat-baby_pj3bnp.jpg',
    'https://res.cloudinary.com/dvhid4k2j/image/upload/v1655420581/davisuko-5E5N49RWtbA-unsplash_d8yuyx.jpg',
    'https://res.cloudinary.com/dvhid4k2j/image/upload/v1655420670/ian-schneider-TamMbr4okv4-unsplash_fgs9ua.jpg',
    'https://res.cloudinary.com/dvhid4k2j/image/upload/v1655420766/annie-spratt-0ZPSX_mQ3xI-unsplash_s1pxcj.jpg'

]
random_pic = profile_pics[randint(0,len(profile_pics) - 1)]

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_image',default=random_pic)
    bio = models.CharField(max_length=150,blank=True)
    country = CountryField(blank=True,null=True)

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
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='vote')

    design = models.IntegerField(default=0,choices=DESIGN_CHOICES)
    usability = models.IntegerField(default=0,choices=USABILITY_CHOICES)
    content = models.IntegerField(default=0,choices=CONTENT_CHOICES)
    average_score = models.DecimalField(max_digits=4,decimal_places=2)
    date_voted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.average_score}'

    


    





    

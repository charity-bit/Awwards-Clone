from rest_framework import serializers
from awwards.models import Project,Profile
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Profile
        fields = ['id','profile_pic','bio','user']
       

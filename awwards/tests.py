from unicodedata import category
from django.test import TestCase

# Create your tests here.
from django.test import TestCase

from django.contrib.auth.models import User

from .models import Project, Tags, Vote,Profile,Category


# Create your tests here.

class UserTestClass(TestCase):

    def setUp(self):
        self.new_user = User.objects.create(
            username = 'charity',
            password = 'pass1',
            email = 'charitynyanchera@gmail.com'
        )

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

    def test_save_method(self):
        self.new_user.save()
        users = User.objects.all()
        self.assertEquals(len(users),1)

    def test_delete_method(self):
        self.new_user.save()
        test_user = User(username = 'testuser',password='qwertyip',email='example@gmail.com')
        test_user.save()
        self.new_user.delete()
        users = User.objects.all()
        self.assertEquals(len(users),1)


class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create(
            username = 'charity',
            password = 'pass1',
            email = 'charitynyanchera@gmail.com'
        )

        # saving user to create profile for
        self.new_user.save()

        # profile instance
        self.new_profile = Profile(user = self.new_user,country = 'KE',bio = "I confess I'm a flex")
    

    

class ProjectTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create(
            username = 'charity',
            password = 'pass1',
            email = 'charitynyanchera@gmail.com'
        )

        # saving user to create profile for
        self.new_user.save()

        self.new_project = Project.objects.create(
            user = self.new_user,
            sitename = 'awwards Clone',
            url = 'http://127.0.0.1:8000/',
            description = 'this is a clone site',
            image = 'https://res.cloudinary.com/dvhid4k2j/image/upload/v1655420766/annie-spratt-0ZPSX_mQ3xI-unsplash_s1pxcj.jpg',
            designer_name = 'charity',
            designer_url = 'http://127.0.0.1:8000/',
            country = 'KE'

            
            )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))

    
    def test_save_project(self):
        self.new_project.save_project()
        projects= Project.objects.all()

        self.assertEquals(len(projects),1)









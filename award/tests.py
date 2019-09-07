from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.

class ProjectClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='Emmanuel')
        self.profile = Profile(username = self.user)
        self.profile.save()
        self.project = Project(id=1,project_image = 'projects/',title='Awards System',post='test the system',owner=self.user,design=5,usability=10,content=9,average_score=8)

#     #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))

#     #Testing Save method
    def test_save_project(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

#     #Testing Update Method
#     def test_update_caption(self):
#         self.image.save_image()
#         self.image = Image.objects.get(pk = 1)
#         self.image.update_caption('updated caption')
#         self.updated_image = Image.objects.get(id = 1)
#         self.assertEqual(self.updated_image.image_caption,"updated caption")

#     #Testing Delete Method
#     def test_delete_image(self):
#         self.image.delete_image()
#         self.assertTrue(len(Image.objects.all()) == 0)

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='Emmanuel')
        self.profile = Profile(id=1,profpic='/profpics/',bio='test bio',username = self.user,email='emmanuel.muchiri@outlook.com')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    # Testing save method
    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
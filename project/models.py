from django.db import models
from django.contrib.auth.models import User

class Roll(models.Model):
    roll = models.CharField(max_length=50)
    
class Tag(models.Model):
    tag = models.CharField(max_length=50)
    

class Project(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True, default='Untitled')
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True, default='static/images/proj1.svg')
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True, related_name='tag_projects')

    
class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memberships', blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='project_members', blank=True, null=True)
    roll = models.ForeignKey(Roll, on_delete=models.SET_NULL, blank=True, null=True, related_name='roll_members')

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tasks', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_tasks', blank=True, null=True)
    done = models.BooleanField(default=False)
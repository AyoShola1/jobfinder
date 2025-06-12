# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_recruiter = models.BooleanField(default=False)
    is_job_seeker = models.BooleanField(default=False)
    profile_picture = models.ImageField( upload_to='profile_pics', blank=True, default='profile_pics/default.jpg')
    
    resume = models.FileField(upload_to='resumes', blank=True)
    bio = models.TextField(blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    

    def __str__(self):
        return self.username
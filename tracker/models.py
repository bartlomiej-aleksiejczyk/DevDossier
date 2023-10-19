from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    avatarPath = models.CharField(max_length=255, blank=True, null=True)
    dateJoined = models.DateTimeField(auto_now_add=True)
    lastLogin = models.DateTimeField(auto_now=True)


class App(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apps', null=True)


class Entry(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')
    status = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    repoLink = models.URLField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=True)
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='entries')


class Tag(models.Model):
    tagString = models.CharField(max_length=100)
    tagColor = models.CharField(max_length=7)
    entry = models.ManyToManyField(Entry, related_name='tags')


class Comment(models.Model):
    body = models.TextField()
    attachment = models.OneToOneField('Attachment', on_delete=models.SET_NULL, blank=True, null=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='comments')


class Attachment(models.Model):
    filePath = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attachments')

    def checkIfValid(self):
        pass

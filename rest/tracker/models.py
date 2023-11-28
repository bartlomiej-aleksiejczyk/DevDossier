from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from tracker.enums.entry_enums import EntryStatus, EntryType, EntryPriority


class TrackerUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    objects = TrackerUserManager()

    username = models.CharField(max_length=150, unique=True)
    avatarPath = models.CharField(max_length=255, blank=True, null=True, default="https://u.cubeupload.com/dawid8374/genericavatar.png")
    dateJoined = models.DateTimeField(auto_now_add=True)
    lastLogin = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'


class App(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    repoLink = models.URLField(blank=True, null=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apps', null=True)


class Entry(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(
        max_length=50,
        choices=[(type_.name, type_.value) for type_ in EntryType],
        default=EntryType.TYPE1.name
    )
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries', null=True)
    status = models.CharField(
        max_length=50,
        choices=[(status.name, status.value) for status in EntryStatus],
        default=EntryStatus.NEW.name
    )
    priority = models.CharField(
        max_length=50,
        choices=[(priority.name, priority.value) for priority in EntryPriority],
        default=EntryPriority.MEDIUM.name
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=True)
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='entries')


class Tag(models.Model):
    tagName = models.CharField(max_length=100)
    tagColor = models.CharField(max_length=7)
    entry = models.ManyToManyField(Entry, related_name='tags')

    def __str__(self):
        return self.tagName


class Comment(models.Model):
    body = models.TextField()
    attachment = models.OneToOneField('Attachment', on_delete=models.SET_NULL, blank=True, null=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='comments')


class Attachment(models.Model):
    filePath = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attachments', null=True)

    def check_if_valid(self):
        pass

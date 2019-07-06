from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE


class FriendList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_id = models.PositiveIntegerField(null=True)


class Group(models.Model):
    group_name = models.CharField(max_length=200, help_text='Enter a Group name', null=True)
    group_description = models.TextField(max_length=1000, help_text='Enter a Group description', null=True)
    total_member = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Event(models.Model):
    event_name = models.CharField(max_length=200, help_text='Enter a Event name', null=True)
    event_description = models.TextField(max_length=1000, help_text='Enter a event description', null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

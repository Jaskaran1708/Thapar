from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# class CustomUser(AbstractUser):
#     phone_number = models.IntegerField(unique=True)
#     email = models.EmailField(null=True, blank=True)

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, max_length=254, null=True)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='customuser',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
        verbose_name='user permissions'
    )

class Contact(models.Model):
    username = models.ForeignKey(CustomUser, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

class SpamReport(models.Model):
    phone_number = models.CharField(max_length=15)
    reporter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

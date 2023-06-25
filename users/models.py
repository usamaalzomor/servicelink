from django.contrib.auth.models import User
from django.db import models


class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    date_of_birth = models.DateField(null=True, blank=True)
    specialization = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.user_profile.user.username

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.user_profile.user.username

class EmployeeAssistant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user_profile.user.username
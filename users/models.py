from django.contrib.auth.models import User
from django.db import models

class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    experience_years = models.IntegerField()

    def __str__(self):
        return self.user.username

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=250)  # Will enhance it to an actual geo location.

    def __str__(self):
        return self.user.username

class EmployeeAssistant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    supervisor = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
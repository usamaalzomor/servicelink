from django.db import models
from users.models import Customer, Technician
from django.core.validators import MinValueValidator

# Create your models here.

class ServiceOrder(models.Model):
    SCHEDULED = "SC"
    INPROGRESS = "IP"
    COMPLETED = "CO"
    STATUS_CHOICES = [
        (SCHEDULED, 'Scheduled'),
        (INPROGRESS, 'In progress'),
        (COMPLETED, 'Completed')
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.PROTECT)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    scheduled_time = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()


class Service(models.Model):
    INSTALLATION = "IN"
    MAINTENANCE = "MA"
    REPAIR = "RE"
    SERVICE_TYPE_CHOICES = [
        (INSTALLATION, 'Installation'),
        (MAINTENANCE, 'Maintenance'),
        (REPAIR, 'Repair')
    ]

    service_type = models.CharField(max_length=2, choices=SERVICE_TYPE_CHOICES)
    unit_price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField()


class ServiceOrderItem(models.Model):
    service_order = models.ForeignKey(ServiceOrder, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)



from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tour(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tours")
    tour_category = models.CharField(max_length=255)
    start_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    price_per_person = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    seats = models.IntegerField()
    vehicle = models.CharField(max_length=255)
    descriptions = models.TextField(null=True)
    pickup_point = models.CharField(max_length=255)
    latitude  = models.DecimalField(max_digits=9, decimal_places=6,null=True)
    longitude  = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


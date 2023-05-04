from django.db import models

from restaurants.models import Restaurants


class Menu(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300, blank=True)
    price = models.FloatField()
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)

    def __str__(self):
        return f'name of the dish: {self.name}, description: {self.description}, price: {self.price}'

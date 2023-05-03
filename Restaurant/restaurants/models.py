from django.db import models


class Restaurants(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

    def __str__(self):
        return f'name: {self.name}, address: {self.address}'

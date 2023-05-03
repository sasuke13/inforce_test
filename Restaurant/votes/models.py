from django.db import models

from authentication.models import CustomUser
from restaurants.models import Restaurants


class Votes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)

    def __str__(self):
        return f'User {self.user} voted for {self.restaurant} restaurant'

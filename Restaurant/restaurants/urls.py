from django.urls import path
from .views import *

urlpatterns = [
    path('', RestaurantAPIListView.as_view()),
    path('<int:pk>/', RestaurantAPIUpdateDelete.as_view())
]
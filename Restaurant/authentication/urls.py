from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', TokenPairView.as_view(), name='token_obtain_view'),
    path('registration/', RegisterView.as_view(), name='token_obtain_view'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
]

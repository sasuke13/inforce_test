from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_view'),
    # path('', CustomLoginView.as_view(), name='login'),
    # path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('registration/', RegisterView.as_view(), name='token_obtain_view'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
]

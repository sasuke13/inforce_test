from django.urls import path

from menu.views import MenuListCreateAPIView, MenuUpdateDeleteAPIView, TodayMenuListCreateAPIView

urlpatterns = [
    path('', TodayMenuListCreateAPIView.as_view()),
    path('all/', MenuListCreateAPIView.as_view()),
    path('<int:pk>/', MenuUpdateDeleteAPIView.as_view())
]

from django.urls import path

from votes.views import VoteAPIView, ResultsAPIView

urlpatterns = [
    path('', VoteAPIView.as_view()),
    path('results/', ResultsAPIView.as_view()),
]
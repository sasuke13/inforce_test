from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from votes.models import Votes
from votes.permissions import IsAdmin
from votes.serializers import VoteSerializer, ResultSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication


class VoteAPIView(generics.CreateAPIView):
    model =Votes
    serializer_class = VoteSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAdmin, )


class ResultsAPIView(APIView):

    def get(self, request, *args, **kwargs):
        votes = Votes.objects.all()
        results = {}

        for vote in votes:
            if vote.restaurant in results:
                results[vote.restaurant] += 1
            else:
                results.update({vote.restaurant: 1})

        results_lst = [{"restaurant": k, "votes": v} for k, v in results.items()]
        serializer = ResultSerializer(results_lst, many=True)
        return Response(serializer.data)

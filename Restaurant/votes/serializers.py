from rest_framework import serializers

from votes.models import Votes


class VoteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Votes
        fields = '__all__'

    def validate(self, data):
        user = self.context['request'].user
        restaurant = data['restaurant']
        vote = Votes.objects.filter(user=user)

        if not user.is_staff:
            if vote.exists():
                vote = vote.first()
                if vote.restaurant == restaurant:
                    raise serializers.ValidationError("You already voted for this restaurant, you can change your mind and choose another restaurant")
                vote.restaurant = restaurant
                vote.save()
                raise serializers.ValidationError("Your vote was changed")

            return data

        raise serializers.ValidationError("Admins cannot vote!")


class ResultSerializer(serializers.Serializer):
    restaurant = serializers.CharField()
    votes = serializers.IntegerField()

from rest_framework import serializers
from .models import Game

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ("id", "title", "release_date", "score", "description", "metacritic_link", "must_paly", "genre", "platform", "company")
         
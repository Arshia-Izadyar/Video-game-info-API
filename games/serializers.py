from rest_framework import serializers
from .models import Game
from review.serializers import CommentSerializer

class GamesSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    def to_representation(self, instance):
        resp =  super().to_representation(instance)
        request = self.context.get("request")
        if not request.parser_context["kwargs"]:
           resp.pop("description") 
           resp.pop("metacritic_link") 
           resp.pop("image") 
           resp.pop("score")
           resp.pop("comments")
           return resp
        return resp

    class Meta:
        model = Game
        fields = ("id", "title", "release_date", "score", "description", "metacritic_link", "must_play", "genre", "platform", "company", "image", "comments")
         
         
    
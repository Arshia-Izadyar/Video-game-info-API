from rest_framework import serializers
from django.db.models import Avg
from .models import Game, HowLongToBeat, BookMark
from review.serializers import CommentSerializer, UserSerializer


class GamesSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    user_rate = serializers.SerializerMethodField()
    hltb_normal = serializers.SerializerMethodField()
    hltb_hard = serializers.SerializerMethodField()
    hltb_full = serializers.SerializerMethodField()

    def to_representation(self, instance):
        resp = super().to_representation(instance)
        request = self.context.get("request")
        if not request.parser_context["kwargs"]:
            resp.pop("description")
            resp.pop("metacritic_link")
            resp.pop("image")
            resp.pop("score")
            resp.pop("comments")
            return resp
        return resp

    def get_hltb_normal(self, obj):
        time = obj.hltb.filter(mode=2).aggregate(avg_time=Avg("time"))["avg_time"]
        if time is not None:
            time = time // 3600
        else:
            time = 0
        return time

    def get_hltb_hard(self, obj):
        time = obj.hltb.filter(mode=3).aggregate(avg_time=Avg("time"))["avg_time"]
        if time is not None:
            time = time // 3600
        else:
            time = 0
        return time

    def get_hltb_full(self, obj):
        time = obj.hltb.filter(mode=1).aggregate(avg_time=Avg("time"))["avg_time"]
        if time is not None:
            time = time // 3600
        else:
            time = 0
        return time

    def get_user_rate(self, obj):
        rate = obj.rates.aggregate(avg_rate=Avg("rate"))["avg_rate"]
        return rate

    class Meta:
        model = Game
        fields = (
            "id",
            "title",
            "user_rate",
            "release_date",
            "score",
            "hltb_normal",
            "hltb_hard",
            "hltb_full",
            "description",
            "metacritic_link",
            "must_play",
            "genre",
            "platform",
            "company",
            "image",
            "comments",
        )


class HowLongToBeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowLongToBeat
        fields = ("time", "mode")


class BookMarkSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = BookMark
        fields = ("user", )
        
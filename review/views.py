from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from games.models import Game
from .serializers import CommentSerializer, RateSerializer



class AddComment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            obj = Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            return Response({"Error": "Game does not exist."}, status=status.HTTP_404_NOT_FOUND)

        user = self.request.user
        if obj.allow_comment(user):
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=user, game=obj)
                return Response({"Status": "Done"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"Status":{"Error":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Status":{"Error":serializer.errors}}, status=status.HTTP_406_NOT_ACCEPTABLE)

        
class RateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        game_object = get_object_or_404(Game, pk=pk)
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, game=game_object)
            return Response({"Status":"Done"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Status":{"Error":serializer.errors}}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
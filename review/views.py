from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from games.models import Game
from . models import Comment
from .serializers import CommentSerializer, RateSerializer



class Comment(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, game_pk, comment_pk=None):
        if comment_pk is None:
            comments = Comment.objects.filter(game__pk=game_pk, parent__isnull=True)
            serialized = CommentSerializer(comments, many=True)

            return Response({"comments":serialized.data}, status=status.HTTP_202_ACCEPTED)
        else:
            try:
                comment = Comment.objects.get(pk=comment_pk)
                serialized = CommentSerializer(comment)
                replies = Comment.objects.filter(parent=comment)
                reply_serialized = CommentSerializer(replies, many=True)
                return Response({"Comment":serialized.data, "replies":reply_serialized.data}, status=status.HTTP_202_ACCEPTED)
            except Comment.DoesNotExist:
                return Response({"status":{"Error" :"Cant get the comment"}}, status=status.HTTP_404_NOT_FOUND)
    

    def post(self, request, game_pk, comment_pk=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            game_obj = get_object_or_404(Game, pk=game_pk)
            user = request.user
            parent_comment=None
            if comment_pk is not None:
                try :
                    parent_comment = get_object_or_404(Comment, pk=comment_pk)
                except Comment.DoesNotExist:
                    return Response({"status":{"Error":"Parent Comment not Found"}}, status=status.HTTP_404_NOT_FOUND)
            serializer.save(game=game_obj, user=user, parent=parent_comment)
            return Response({"status":"Done"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Status":{"Error":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST) 
        
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
        
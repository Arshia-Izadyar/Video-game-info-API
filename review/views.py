from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from games.models import Game
from .serializers import CommentSerializer



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
                return Response({"Done": "Created"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": "Can't add more than 3 comments."}, status=status.HTTP_406_NOT_ACCEPTABLE)

        

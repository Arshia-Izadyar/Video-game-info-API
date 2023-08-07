from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from .models import Game, HowLongToBeat, BookMark
from .serializers import GamesSerializer, HowLongToBeatSerializer, BookMarkSerializer
from .paginators import StandardPagination


class GamesListView(ListAPIView):
    serializer_class = GamesSerializer
    queryset = Game.objects.all()
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["genre", "company", "platform"]
    search_fields = ["title"]
    ordering_fields = ["score", "release_date"]



class GameDetailView(RetrieveUpdateAPIView):
    serializer_class = GamesSerializer
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Game.objects.prefetch_related("comments").filter(pk=pk)


class TopGamesListView(ListAPIView):
    serializer_class = GamesSerializer
    permission_classes = [IsAuthenticated]
    queryset = Game.objects.filter(Q(must_play=True) & Q(score__gte=80))[:250]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["genre", "company", "platform"]
    search_fields = ["title"]
    ordering_fields = ["score", "release_date"]


class CategoryListView(ListAPIView):
    serializer_class = GamesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        genre = self.kwargs.get("genre")
        return Game.objects.filter(genre__name__icontains=genre)


class UpdateGameView(APIView):
    permission_classes = [IsAdminUser]
    def patch(self, request, s):
        try:
            obj = get_object_or_404(Game, slug=s)
        except Game.DoesNotExist:
            return Response({"Status":{"Error":"Object not found"}}, status=status.HTTP_404_NOT_FOUND)
        serializer = GamesSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Status": "Done", "Updated":serializer.data}, status=status.HTTP_202_ACCEPTED)
    
class CreateGameView(APIView):
    permission_classes = [IsAdminUser]

    serializer_class = GamesSerializer
    def post(self, request):
        serializer = GamesSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status":"Created","Game":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"Status":{"Error":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
    
    
class HowLongToBeatView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    model = HowLongToBeat
    serializer_class = HowLongToBeatSerializer

    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        game = Game.objects.get(pk=pk)
        serializer.save(user=self.request.user, game=game)
        return Response({"Status": "Created"}, status=status.HTTP_201_CREATED)

class AddBookMarkView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        serializer = BookMarkSerializer(data=request.data)
        if serializer.is_valid():
            game = get_object_or_404(Game, pk=pk)
            serializer.save(user=request.user, game=game)
            return Response({"Status":"Done"}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"Status":{"Error":serializer.errors}})


class BookMarkListView(ListAPIView):
    serializer_class = BookMarkSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return BookMark.objects.filter(user__username=user.username)

class DeleteGame(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self, request, s):
        obj = get_object_or_404(Game, slug=s)
        obj.delete()
        return Response({"Status":"Deleted"}, status=status.HTTP_204_NO_CONTENT)
        
    
        
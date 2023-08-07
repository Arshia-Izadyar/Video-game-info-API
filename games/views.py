from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q


from .models import Game, HowLongToBeat
from .serializers import GamesSerializer, HowLongToBeatSerializer
from .paginators import StandardPagination

class GamesListView(ListAPIView):
    serializer_class = GamesSerializer
    permission_classes = [IsAuthenticated]
    queryset = Game.objects.all()
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genre', 'company', 'platform']
    search_fields = ['title']
    ordering_fields = ["score", "release_date"]

class GameDetailView(RetrieveUpdateAPIView):
    serializer_class = GamesSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Game.objects.prefetch_related("comments").filter(pk=pk) 
    
    
class TopGamesListView(ListAPIView):
    serializer_class = GamesSerializer
    permission_classes = [IsAuthenticated]
    queryset = Game.objects.filter(Q(must_play=True) & Q(score__gte=80))[:250]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genre', 'company', 'platform']
    search_fields = ['title']
    ordering_fields = ["score", "release_date"]
    
class CategoryListView(ListAPIView):
    serializer_class = GamesSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        genre = self.kwargs.get("genre")
        return Game.objects.filter(genre__name__icontains=genre)

    
    
class HowLongToBeatView(CreateAPIView):
    model = HowLongToBeat
    serializer_class = HowLongToBeatSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        game = Game.objects.get(pk=pk)
        serializer.save(user=self.request.user, game=game)
        return Response({"Status":"Created"}, status=status.HTTP_201_CREATED)
    
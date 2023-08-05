from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from .models import Game
from .serializers import GamesSerializer
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


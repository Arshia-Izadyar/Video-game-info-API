from django.urls import path


from .views import GamesListView, GameDetailView

app_name = "game"

urlpatterns = [
    path("list/", GamesListView.as_view(), name="list"),
    path("detail/<int:pk>/", GameDetailView.as_view(), name="detail"),
]

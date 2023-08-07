from django.urls import path


from .views import (GamesListView,
                    GameDetailView,
                    CategoryListView,
                    HowLongToBeatView,
                    TopGamesListView,
                    AddBookMarkView,
                    BookMarkListView,
                    UpdateGameView,
                    CreateGameView,
                    DeleteGame,
                    )
app_name = "game"

urlpatterns = [
    path("create/", CreateGameView.as_view(), name="create"),
    path("update/<slug:s>/", UpdateGameView.as_view(), name="update"),
    path("delete/<slug:s>/", DeleteGame.as_view(), name="delete"),
    path("list/", GamesListView.as_view(), name="list"),
    path("detail/<int:pk>/", GameDetailView.as_view(), name="detail"),
    path("category/<slug:genre>/", CategoryListView.as_view(), name="genre-list"),
    path("bookmark/<int:pk>/", AddBookMarkView.as_view(), name="bookmark-add"),
    path("bookmark/list/", BookMarkListView.as_view(), name="bookmark-list"),
    path("top250/", TopGamesListView.as_view(), name="top250"),
    path("how-long-2-beat/<int:pk>/", HowLongToBeatView.as_view(), name="how-long-to-beat"),
]

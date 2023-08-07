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
    path("v1/create/", CreateGameView.as_view(), name="create"),
    path("v1/update/<slug:s>/", UpdateGameView.as_view(), name="update"),
    path("v1/delete/<slug:s>/", DeleteGame.as_view(), name="delete"),
    
    
    path("v1/list/", GamesListView.as_view(), name="list"),
    path("v1/detail/<int:pk>/", GameDetailView.as_view(), name="detail"),
    path("v1/category/<slug:genre>/", CategoryListView.as_view(), name="genre-list"),
    path("v1/bookmark/<int:pk>/", AddBookMarkView.as_view(), name="bookmark-add"),
    path("v1/bookmark/list/", BookMarkListView.as_view(), name="bookmark-list"),
    path("v1/top250/", TopGamesListView.as_view(), name="top250"),
    path("v1/how-long-2-beat/<int:pk>/", HowLongToBeatView.as_view(), name="how-long-to-beat"),
]

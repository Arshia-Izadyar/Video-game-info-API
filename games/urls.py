from django.urls import path


from .views import GamesListView

app_name = "game"

urlpatterns = [
    path("list/", GamesListView.as_view(), name="list")
]

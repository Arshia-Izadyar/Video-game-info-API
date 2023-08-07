from django.urls import path


from .views import Comments, RateView

urlpatterns = [
    path("comment/<int:game_pk>/<int:comment_pk>/", Comments.as_view(), name="add-comment"),
    path("comment/<int:game_pk>/", Comments.as_view(), name="add-comment"),
    path("rate/<int:pk>/", RateView.as_view(), name="add-rate"),
]

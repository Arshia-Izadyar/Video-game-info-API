from django.urls import path


from .views import Comment,RateView

urlpatterns = [
    path("comment/<int:game_pk>/<int:comment_pk>/", Comment.as_view(), name="add-comment"),
    path("comment/<int:game_pk>/", Comment.as_view(), name="add-comment"),
    path("rate/<int:game_pk>/", RateView.as_view(), name="add-rate"),
]



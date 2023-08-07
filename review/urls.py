from django.urls import path


from .views import AddComment,RateView

urlpatterns = [
    path("comment/<int:pk>/", AddComment.as_view(), name="add-comment"),
    path("rate/<int:pk>/", RateView.as_view(), name="add-rate"),
]



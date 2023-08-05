from django.urls import path


from .views import AddComment

urlpatterns = [
    path("comment/<int:pk>/", AddComment.as_view(), name="add-comment")
]



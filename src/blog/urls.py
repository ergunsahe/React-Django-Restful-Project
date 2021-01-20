from django.urls import path
from .views import BlogPostView, BlogPostRetrieveView, BlogPostCreateView, BlogPostUpdateDeleteView,PostCommentCreateView, PostLikeCreateView

urlpatterns = [
    path('', BlogPostView.as_view(), name="list"),
    path('create/', BlogPostCreateView.as_view(), name="create"),
    path("<str:slug>/", BlogPostRetrieveView.as_view(), name="detail"),
    path("<str:slug>/update/", BlogPostUpdateDeleteView.as_view(), name="update"),
    path('<str:slug>/comment/', PostCommentCreateView.as_view(), name="comment"),
    path('<str:slug>/like/', PostLikeCreateView.as_view(), name="create-comment"),
]

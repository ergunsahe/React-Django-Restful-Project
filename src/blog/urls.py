from django.urls import path
from .views import BlogPostList, BlogUserPostList, BlogPostRetrieveView, BlogPostCreateView, BlogPostUpdateDeleteView,PostCommentCreateView, PostLikeCreateView

urlpatterns = [
    path('', BlogPostList.as_view(), name="list"),
    path('userposts/', BlogUserPostList.as_view(), name="user-post"),
    path('create/', BlogPostCreateView.as_view(), name="create"),
    path("<str:slug>/", BlogPostRetrieveView.as_view(), name="detail"),
    path("<str:slug>/update/", BlogPostUpdateDeleteView.as_view(), name="update"),
    path('<str:slug>/comment/', PostCommentCreateView.as_view(), name="comment"),
    path('<str:slug>/like/', PostLikeCreateView.as_view(), name="create-comment"),
]

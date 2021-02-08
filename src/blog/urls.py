from django.urls import path
from .views import BlogPostList, BlogUserPostList,  BlogPostCreateView, BlogPostDetailView,BlogPostUpdateView, BlogPostDeleteView, PostCommentCreateView, PostLikeCreateView

urlpatterns = [
    path('list/', BlogPostList.as_view(), name="list"),
    path('userposts/', BlogUserPostList.as_view(), name="user-post"),
    path('create/', BlogPostCreateView.as_view(), name="create"),
    path("<str:slug>/detail/", BlogPostDetailView.as_view(), name="detail"),
    path("<str:slug>/update/", BlogPostUpdateView.as_view(), name="update"),
    path("<str:slug>/delete/", BlogPostDeleteView.as_view(), name="delete"),
    path('<str:slug>/comment/', PostCommentCreateView.as_view(), name="comment"),
    path('<str:slug>/like/', PostLikeCreateView.as_view(), name="like"),
]

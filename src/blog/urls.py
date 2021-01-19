from django.urls import path
from .views import BlogPostView, BlogPostUpdateDeleteView

urlpatterns = [
    path('', BlogPostView.as_view(), name="list"),
    path("/<str:slug>/", BlogPostUpdateDeleteView.as_view(), name="detail")
]

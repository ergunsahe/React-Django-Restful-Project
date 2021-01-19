from django.urls import path
from .views import BlogPostView

urlpatterns = [
    path('', BlogPostView.as_view(), name="list")
]

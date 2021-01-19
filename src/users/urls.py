from django.urls import path
from .views import RegisterView, ProfileUpdateView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/<int:id>", ProfileUpdateView.as_view(), name="profile"),
]
from django.urls import path
from .views import RegisterView, Profile_get_update

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", Profile_get_update, name="profile"),
    path("profile/update/", Profile_get_update, name="profile-update"),
    # path('profile/update/', profile_update, name='profile-update'),
]
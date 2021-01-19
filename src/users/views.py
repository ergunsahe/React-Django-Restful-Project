from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics

from users.models import Profile
from .serializers import RegisterSerializer, ProfileSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "id"
    
    # def get_queryset(self):
    #     queryset = Profile.objects.all()
    #     id = self.kwargs["id"]
    #     queryset = queryset.filter(id= id)
        
    #     return queryset
    
    

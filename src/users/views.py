from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from blog import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import Profile
from .serializers import RegisterSerializer, ProfileSerializer, UserSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    

@api_view(['GET', 'PUT'])
def Profile_get_update(request):
    # profile= get_object_or_404(Profile, user__id=id)
    if request.method == 'GET':
        serializer =ProfileSerializer(request.user.profile)
        
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ProfileSerializer(request.user.profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Profile updated succesfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(["PUT"])
# def profile_update(request):
#     p_serializer = ProfileSerializer(request.user.profile, data=request.data)
#     u_serializer = UserSerializer(request.user, data=request.data)
#     if u_serializer.is_valid() and p_serializer.is_valid():
#         u_serializer.save()
#         p_serializer.save()
#         data = {
#             "message": "Profile updated succesfully!"
#         }
#         return Response(data)
#     return Response(u_serializer.errors, p_serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    

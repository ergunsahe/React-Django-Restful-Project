from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from .serializers import BlogPostSerializer
from .models import BlogPost

# Create your views here.

class BlogPostView(ListCreateAPIView):
    serializer_class = BlogPostSerializer  
    queryset = BlogPost.objects.all()
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    
        
class BlogPostUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
    lookup_field = "slug"
    
    
    
    

    

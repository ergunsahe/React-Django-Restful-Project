from django.shortcuts import render
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
    
    

    

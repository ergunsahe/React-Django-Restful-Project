from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .serializers import BlogPostListSerializer, BlogPostCreateUpdateSerializer, CommentCreateSerializer, BlogPostDetailSerializer
from .models import BlogPost, PostComment, PostLike, PostView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .pagination import BlogPostPagePagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwner

# Create your views here.

class BlogPostList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogPostListSerializer  
    queryset = BlogPost.objects.filter(status='p')
    pagination_class = BlogPostPagePagination
    
    
class BlogUserPostList(generics.ListAPIView):
    serializer_class = BlogPostListSerializer  
    pagination_class = BlogPostPagePagination
    permission_classes = [IsAuthenticated, IsOwner]
    # queryset = BlogPost.objects.filter(author=request.user)
    
    def get_queryset(self):
        queryset = BlogPost.objects.filter(author=self.request.user)
        return queryset
    
    
class BlogPostCreateView(generics.CreateAPIView):
    serializer_class = BlogPostCreateUpdateSerializer  
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    
    def perform_create(self, serializer):
        
        serializer.save(author=self.request.user)
        
    
        
class BlogPostDetailView(generics.RetrieveAPIView):
    serializer_class = BlogPostDetailSerializer
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "slug"
    
    def get_object(self):
        obj = super().get_object()
        PostView.objects.get_or_create(author=self.request.user, post=obj)
        return obj
    

class BlogPostUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = BlogPostCreateUpdateSerializer
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = "slug"
    
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
        
class BlogPostDeleteView(generics.DestroyAPIView):
    serializer_class = BlogPostDetailSerializer
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = "slug"
    
   
        
        
    

class PostCommentCreateView(APIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]
    # queryset = PostComment.objects.all()
    
    def post(self, request, slug):
        post= get_object_or_404(BlogPost, slug=slug)
        serializer= CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=200)
        else:
            return Response({'errors': serializer.errors}, status=400)
    
class PostLikeCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, slug):
        obj = get_object_or_404(BlogPost, slug=slug)
        like_qs = PostLike.objects.filter(author=request.user, post=obj)
        
        if like_qs.exists():
            like_qs[0].delete()
        else:
            PostLike.objects.create(author=request.user, post=obj)
            
        
        data = {
            'messages': 'like'
        }
        
        return Response(data)
    
    
    
    

    

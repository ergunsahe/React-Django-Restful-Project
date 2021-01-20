from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .serializers import BlogPostListSerializer, BlogPostCreateSerializer, CommentSerializer, BlogPostDetailSerializer, BlogPostUpdateSerializer, LikeSerializer
from .models import BlogPost, PostComment, PostLike
from .pagination import BlogPagination
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

class BlogPostView(generics.ListAPIView):
    serializer_class = BlogPostListSerializer  
    queryset = BlogPost.objects.all()
    pagination_class = BlogPagination
    permission_classes = [AllowAny]
    
    def perform_create(self, serializer):
        
        serializer.save(author=self.request.user)
class BlogPostCreateView(generics.CreateAPIView):
    serializer_class = BlogPostCreateSerializer  
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        
        serializer.save(author=self.request.user)
        
    
        
class BlogPostRetrieveView(generics.RetrieveAPIView):
    serializer_class = BlogPostDetailSerializer
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "slug"
    

class BlogPostUpdateDeleteView(generics.UpdateAPIView):
    serializer_class = BlogPostUpdateSerializer
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "slug"
    

class PostCommentCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = PostComment.objects.all()
    lookup_field = "post"
    
class PostLikeCreateView(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    # queryset = PostLike.objects.all()
    
    # def perform_create(self, serializer):
        
    #     serializer.save(author=self.request.user)
    
    def get_queryset(self):
        author = self.request.user
        return User.objects.filter(author)
        
    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.multiple_lookup_fields:
            filter["id"] = self.kwargs["id"]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj
    
    
    
    

    

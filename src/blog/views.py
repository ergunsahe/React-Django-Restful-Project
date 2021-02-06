from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .serializers import BlogPostListSerializer, BlogPostCreateSerializer, CommentSerializer, BlogPostDetailSerializer, BlogPostUpdateSerializer, LikeSerializer
from .models import BlogPost, PostComment, PostLike
from .pagination import BlogPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwner

# Create your views here.

class BlogPostList(generics.ListAPIView):
    serializer_class = BlogPostListSerializer  
    queryset = BlogPost.objects.filter(status='p')
    pagination_class = BlogPagination
    permission_classes = [AllowAny]
    
    
class BlogUserPostList(generics.ListAPIView):
    serializer_class = BlogPostListSerializer  
    pagination_class = BlogPagination
    permission_classes = [IsAuthenticated, IsOwner]
    # queryset = BlogPost.objects.filter(author=request.user)
    
    def get_queryset(self):
        queryset = BlogPost.objects.filter(author=self.request.user)
        return queryset
    
    
class BlogPostCreateView(generics.CreateAPIView):
    serializer_class = BlogPostCreateSerializer  
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    
    def perform_create(self, serializer):
        
        serializer.save(author=self.request.user)
        
    
        
class BlogPostRetrieveView(generics.RetrieveAPIView):
    serializer_class = BlogPostDetailSerializer
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "slug"
    

class BlogPostUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogPostUpdateSerializer
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "slug"
    

class PostCommentCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = PostComment.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "post"
    
class PostLikeCreateView(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    queryset = PostLike.objects.all().select_related('postlike')
    
    # def get_queryset(self):
    #     queryset = PostLike.objects.all()
    #     post = BlogPost.objects.all()
    #     slug= self.kwargs["slug"]
    #     post = post.filter(blogpost__slug= slug)
    #     queryset = queryset.filter(post =post)
    #     return queryset
    
    
    
    
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
    
    # def get_queryset(self):
    #     user = self.request.user
    #     queryset= User.objects.filter(__username=user)
    #     return queryset
    
        
        
    # def get_object(self):
    #     queryset = self.get_queryset()
    #     filter = {}
    #     for field in self.multiple_lookup_fields:
    #         filter["id"] = self.kwargs["id"]

    #     obj = get_object_or_404(queryset, **filter)
    #     self.check_object_permissions(self.request, obj)
    #     return obj
    
    
    
    

    

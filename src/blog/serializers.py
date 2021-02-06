from django.contrib.auth.models import User
from rest_framework import fields, serializers
from .models import BlogPost, PostComment, PostLike





    

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField( source="author.username", read_only=True)
    class Meta:
        model = PostComment
        fields = ( "content",  "author",)
        read_only_fields = ["post","create_date"]
        
        
class CommentCreateSerializer(serializers.Serializer):
    content = serializers.CharField()
    author = serializers.CharField( source="author.username", read_only=True)
    class Meta:
        model = PostComment
        fields = ( "content", "post", "author")
        read_only_fields = ["post","author"]
        
        
        
        
class BlogPostListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name ='detail',
        lookup_field = 'slug',
        
    )
    author = serializers.CharField( source="author.username", read_only=True)
    comments = CommentSerializer(many=True)
    
    class Meta:
        model = BlogPost
        fields = ("url",  "id", "title", "content", "image", "status", 'author', 'comment_count', 'view_count', 'like_count', 'comments')
        read_only_fields = ['author', "create_date", "update_date","slug"]
        
        
        
class LikeSerializer(serializers.ModelSerializer):
    # post =serializers.SlugField(source="post.slug", read_only=True)
    author = serializers.CharField( source="author.username", read_only=True)
    class Meta:
        model = PostLike
        fields = ("author", "post")
class BlogPostCreateSerializer(serializers.ModelSerializer):
    
    author = serializers.CharField( source="author.username", read_only=True)
    class Meta:
        model = BlogPost
        fields = ( "title", "content", "image", "status", 'author')
        
        
        
class BlogPostDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name ='detail',
        lookup_field = 'slug',
        
    )
    author = serializers.CharField( source="author.username", read_only=True)
    comments = CommentSerializer(many=True)
    
    class Meta:
        model = BlogPost
        fields = ("url",  "title", "content", "image", "status", 'author', 'comment_count', 'view_count', 'like_count', 'comments')
        read_only_fields = ['author', "create_date", "update_date","slug"]
        
        
class BlogPostUpdateSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name ='detail',
        lookup_field = 'slug',
        
    )
    author = serializers.CharField( source="author.username", read_only=True)
    
    
    class Meta:
        model = BlogPost
        fields = ("url",  "title", "content", "image", "status", 'author', 'comment_count', 'view_count', 'like_count', )
        read_only_fields = ['author', "create_date", "update_date","slug",]
        

        
        
    
        
        
   
        
            
        
    
        

    
        
        
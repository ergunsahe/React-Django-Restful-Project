from django.contrib.auth.models import User
from rest_framework import fields, serializers
from .models import BlogPost, PostComment, PostLike
from django.http import request
from django.db.models import Q


    

class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.CharField( source="author.username", read_only=True)
    # status = serializers.ChoiceField(choices=BlogPost.OPTIONS)
    author= serializers.StringRelatedField()
    post= serializers.StringRelatedField()
    class Meta:
        model = PostComment
        fields = ('id', "content",  "author", 'post', 'create_date')
        read_only_fields = ["post","create_date"]
        
        
class CommentCreateSerializer(serializers.ModelSerializer):
    # content = serializers.CharField()
    # author = serializers.CharField( source="author.username", read_only=True)
    class Meta:
        model = PostComment
        fields = ( "content",)
        read_only_fields = ["post","author"]
        
        
class BlogPostDetailSerializer(serializers.ModelSerializer):
    # author = serializers.CharField( source="author.username", read_only=True)
    author = serializers.SerializerMethodField()
    status = serializers.ChoiceField(choices=BlogPost.OPTIONS)
    has_liked = serializers.SerializerMethodField()
    # like= LikeSerializer(many=True)
    comments = CommentSerializer(many=True)
    owner =serializers.SerializerMethodField(read_only=True)
    update_url = serializers.HyperlinkedIdentityField(
        view_name ='update',
        lookup_field = 'slug',
        
    )
    like_url = serializers.HyperlinkedIdentityField(
        view_name ='like',
        lookup_field = 'slug',
        
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name ='delete',
        lookup_field = 'slug',
        
    )
    comment_url = serializers.HyperlinkedIdentityField(
        view_name ='comment',
        lookup_field = 'slug',
        
    )
    
    class Meta:
        model = BlogPost
        fields = (
            'like_url',
            'update_url',
            'delete_url',
            'comment_url',  
            "id",
            "create_date",
            "update_date",
            "title", 
            "content", 
            "image", 
            "status", 
            'author', 
            "slug",
            'comment_count', 
            'view_count', 
            'like_count', 
            'comments',
            "owner",
            "has_liked"
            )
        # read_only_fields = ['author', "create_date", "update_date","slug"]   
        
        def get_author(self, obj):
            return obj.author.username
        
        def get_owner(self,obj):
            request= self.context['request']
            if request.user.is_authenticated:
                if obj.author == request.user:
                    return True
                return False
            
        def get_has_liked(self, obj):
            request=self.context['request']
            if request.user.is_authenticated:
                if BlogPost.objects.filter(Q(like_user=request.user) & Q(like_post=obj)).exists():
                    return True
                return False     
        
class BlogPostListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name ='detail',
        lookup_field = 'slug',
        
    )
    author = serializers.SerializerMethodField()
    # author = serializers.CharField( source="author.username", read_only=True)
    # comments = CommentSerializer(many=True)
    
    class Meta:
        model = BlogPost
        fields = (
            "url",  
            "id", 
            "title", 
            "content", 
            "image", 
            "status", 
            'author', 
            'create_date',
            'view_count',
            'slug',
            'comment_count',
            "like_count"
            )
        # read_only_fields = ['author', "create_date", "update_date","slug"]
        
    def get_author(self, obj):
        return obj.author.username
        
        

        
        
class BlogPostCreateUpdateSerializer(serializers.ModelSerializer):
    # author = serializers.CharField( source="author.username", read_only=True)
    owner = serializers.SerializerMethodField(read_only=True)
    
    
    class Meta:
        model = BlogPost
        fields = (
            "id", 
            "title", 
            "content", 
            "image", 
            "status", 
            'owner'
            )
        
    def get_owner(self, obj):
        request=self.context['request']
        if request.user.is_authenticated:
            if obj.author == request.user:
                return True
            return False
        
    
        
        
        

        
# class BlogPostUpdateSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(
#         view_name ='detail',
#         lookup_field = 'slug',
        
#     )
#     author = serializers.CharField( source="author.username", read_only=True)
#     owner = serializers.SerializerMethodField(read_only=True)
    
    
#     class Meta:
#         model = BlogPost
#         fields = ("url",  "title", "content", "image", "status", 'author', 'comment_count', 'view_count', 'like_count', )
#         read_only_fields = ['author', "create_date", "update_date","slug",]
    
#     def get_owner(self, obj):
#         request=self.context['request']
#         if request.user.is_authenticated:
#             if obj.author == request.user:
#                 return True
#             return False
        

        
        
# class LikeSerializer(serializers.ModelSerializer):
#     # post =serializers.SlugField(source="post.slug", read_only=True)
#     author = serializers.CharField( source="author.username", read_only=True)
#     class Meta:
#         model = PostLike
#         fields = ("author", "post")
    
        
        
   
        
            
        
    
        

    
        
        
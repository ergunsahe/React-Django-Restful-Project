from django.contrib.auth.models import User
from rest_framework import fields, serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name ='detail',
        lookup_field = 'slug',
        
    )
    author = serializers.CharField( source="author.username", read_only=True)
    class Meta:
        model = BlogPost
        fields = ("url",  "title", "content", "image", "status", 'author', 'comment_count', 'view_count', 'like_count')
        read_only_fields = ['author', "create_date", "update_date","slug"]
        
    
        
        
   
        
            
        
    
        

    
        
        
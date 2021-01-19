from django.contrib.auth.models import User
from rest_framework import fields, serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ("title", "content", "image", "status", 'author')
        read_only_fields = ['author', "create_date", "update_date"]
        
    # def create(self, validated_data):
        
    #     serializer = BlogPost.objects.create(
    #         title = validated_data["title"],
    #         content = validated_data["content"],
    #         image = validated_data["image"] or 'https://picsum.photos/200/300.jpg',
    #         status = validated_data["status"],
            
    #     )
        
    #     serializer.save()
    #     return serializer
        
        
        
   
        
            
        
    
        

    
        
        
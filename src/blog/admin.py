from django.contrib import admin
from .models import BlogPost, PostComment, PostLike, PostView

admin.site.register(BlogPost)
admin.site.register(PostComment)
admin.site.register(PostLike)
admin.site.register(PostView)

# Register your models here.

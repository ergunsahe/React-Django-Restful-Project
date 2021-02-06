from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class BlogPost(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.URLField(max_length=5000, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)
    
       
    
    def __str__(self):
        return self.title
    
    @property
    def comment_count(self):
        return self.postcomment_set.all().count()

    @property
    def view_count(self):
        return self.postview_set.all().count()
    @property
    def like_count(self):
        return self.postlike_set.all().count()
    @property
    def comments(self):
        return self.postcomment_set.all()
    
class PostComment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author.username
    
    
class PostLike(models.Model):
    author = models.ForeignKey(User, related_name="postlike", on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, related_name="postlike", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author.username


class PostView(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author.username
    


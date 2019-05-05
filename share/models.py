from django.db import models

from django.conf import settings

# Create your models here.
class Content(models.Model):
     image = models.ImageField()
     title = models.CharField(max_length=200)
     relay = models.TextField()
     tag_set = models.ManyToManyField('Tag', blank=True)
     content = models.TextField()

     created_at = models.DateTimeField(auto_now_add = True)
     updated_at = models.DateTimeField(auto_now = True)
     
     def __str__(self):
          return self.title
          
class Tag(models.Model):
    name = models.CharField(max_length=140, unique=True)
    
  
class Post(models.Model):
     like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_user_set', through='Like')

     @property
     def like_count(self):
          return self.like_user_set.count()


class Like(models.Model):
      post = models.ForeignKey(Post)
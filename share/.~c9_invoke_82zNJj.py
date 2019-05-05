from django.db import models

# Create your models here.
class Content(models.Model):
     image = models.ImageField()
     title = models.CharField(max_length
     relay = models.TextField()
    
     content = models.CharField(max_length=140, help_text="최대 140자 입력 가능")

     created_at = models.DateTimeField(auto_now_add = True)
     updated_at = models.DateTimeField(auto_now = True)
     
     
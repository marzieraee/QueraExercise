from django.db import models
from django.utils import timezone as tz




    
class Author(models.Model):
    name=models.CharField(max_length=50)
    

class BlogPost(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='blogposts')
    title = models.TextField(max_length=250)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
          
    
    def copy(self):
        new_post = BlogPost()
        new_post.title = self.title
        new_post.body = self.body
        new_post.author = self.author
        new_post.data_created = tz.now()
        new_post.save()
        return new_post.id



class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='comments')
    text = models.TextField(max_length=500)

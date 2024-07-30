from django.db import models # type: ignore

# Create your models here.

class Comment(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    body = models.CharField(max_length=150)
class Post(models.Model):
    name = models.CharField(max_length=30)
    #image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
class Group(models.Model):
    topic = models.CharField(max_length=25)
    members = models.IntegerField()
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.topic
class User(models.Model):
    name = models.CharField(max_length=18)
    lastname = models.CharField(max_length=30)
    profile_pic = models.FileField(upload_to=None, max_length=100)
    description = models.TextField()
    registered_in = models.DateTimeField(auto_now_add=True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)   
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    
    def __str__(self):
        return self.name
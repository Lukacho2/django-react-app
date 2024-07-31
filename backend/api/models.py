from django.db import models

class Comment(models.Model):
    date = models.DateField(auto_now_add=True)
    core = models.CharField(max_length=150, null=False)

class Post(models.Model):
    name = models.CharField(max_length=30)
    core = models.CharField(max_length=150, default='write something', null=False)
    body = models.TextField(default='default body text')
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)

class Group(models.Model):
    topic = models.CharField(max_length=25)
    members = models.IntegerField(default=0)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.topic

class User(models.Model):
    firstname = models.CharField(max_length=18)
    lastname = models.CharField(max_length=30)
    password = models.CharField(max_length=16)
    description = models.TextField()
    registered_in = models.DateTimeField(auto_now_add=True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname

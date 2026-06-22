from django.db import models
from django.contrib.auth.models import User 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=150)
    bio = models.TextField(blank=True)
    avatar = models.URLField(blank=True)
    
    following = models.ManyToManyField(
        "self", 
        related_name="followers", 
        symmetrical=False, 
        blank=True
    )
    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    image = models.URLField()
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Bài đăng của {self.author.user.username}"
    
    
    
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
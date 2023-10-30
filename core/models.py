from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=100)
    text_content = models.TextField(blank=True, null=True)  # Field for text content
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Field for image
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)  # Field for video
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def has_image(self):
        return self.image and hasattr(self.image, 'url') and self.image.url

    def has_video(self):
        return self.video and hasattr(self.video, 'url') and self.video.url

    def __str__(self):
        return f'{self.user}\'s Post {self.id}'

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
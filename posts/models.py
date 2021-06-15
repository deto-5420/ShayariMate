import random
from django.conf import settings
from django.db import models
from django.db.models import Q

User = settings.AUTH_USER_MODEL

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class PostQuerySet(models.QuerySet):
    def by_username(self, username):
        return self.filter(user__username__iexact=username)

    def feed(self, user):
        profiles_exist = user.following.exists()
        followed_users_id = []
        if profiles_exist:
            followed_users_id = user.following.values_list("user__id", flat=True) # [x.user.id for x in profiles]
        return self.filter(
            Q(user__id__in=followed_users_id) |
            Q(user=user)
        ).distinct().order_by("-timestamp")

class PostManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return PostQuerySet(self.model, using=self._db)

    def feed(self, user):
        return self.get_queryset().feed(user)

class Post(models.Model):
    """
    Post by the user in the form of audio and text files

    Args:
        models ([Class]): [models in pyhton are subclassed by Post]
    """
    
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets") # many users can many tweets
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=PostLike)
    content = models.TextField(blank=True, null=True)
    audio = models.FileField(upload_to='audio/', blank=True, null=True) # Reference for templates <audio src="{{ song.file.url }}" autoplay></audio>
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = PostManager()
    # def __str__(self):
    #     return self.content
    
    class Meta:
        ordering = ['-id']
    
    @property
    def is_retweet(self):
        return self.parent != None
    
    def serialize(self):
        '''
        Feel free to delete!
        '''
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }
from shayari_mate import settings 
from rest_framework import serializers
from profiles.serializers import PublicProfileSerializer
from .models import Post

MAX_Post_LENGTH = settings.MAX_Post_LENGTH
Post_ACTION_OPTIONS = settings.Post_ACTION_OPTIONS

class PostActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        value = value.lower().strip() # "Like " -> "like"
        if not value in Post_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for posts")
        return value


class PostCreateSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True) # serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Post
        fields = ['user', 'id', 'content','audio', 'likes', 'timestamp']
    
    def get_likes(self, obj):
        return obj.likes.count()
    
    def validate_content(self, value):
        if len(value) > MAX_Post_LENGTH:
            raise serializers.ValidationError("This Post is too long")
        return value

    # def get_user(self, obj):
    #     return obj.user.id


class PostSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    parent = PostCreateSerializer(read_only=True)
    class Meta:
        model = Post
        fields = [
                'user', 
                'id', 
                'content',
                'likes',
                'is_rePost',
                'parent',
                'audio',
                'timestamp']

    def get_likes(self, obj):
        return obj.likes.count()

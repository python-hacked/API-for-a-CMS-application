from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "description",
            "content",
            "creation_date",
            "owner",
            "is_public",
            "likes_count",
        ]
        read_only_fields = ["likes_count"]

    def get_likes_count(self, obj):
        return obj.like_set.count()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "post", "user"]

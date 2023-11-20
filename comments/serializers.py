from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'is_user',
            'profile_id',
            'profile_image',
            'post',
            'created_at',
            'modified_at',
            'description',
        ]


class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='post.id')

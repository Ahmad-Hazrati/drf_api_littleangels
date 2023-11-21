from rest_framework import serializers
from .models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size is larger than 2MB!'
                )

        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width is larger than 4096px!'
                )

        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height is larger than 4096px!'
                )       
        return value

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                user=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'user', 'is_user', 'profile_id', 'profile_image',
            'created_at', 'modified_at', 'title', 'description',
            'image', 'image_filter', 'like_id', 'likes_count', 'comments_count',
        ]

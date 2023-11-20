from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')

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

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'is_user',
            'profile_id',
            'profile_image',
            'created_at',
            'modified_at',
            'title',
            'description',
            'image',
            'image_filter',
        ]

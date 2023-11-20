from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'is_user', 'profile_id', 'profile_image', 'created_at', 'modified_at', 'title', 'description','image',
        ]
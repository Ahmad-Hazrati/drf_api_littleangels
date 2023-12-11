from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Profile model, providing a way to convert
    Profile instances to and from JSON format.
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_user(self, obj):
        """
        Custom method to determine if the current user is the owner of the profile.

        Args:
        - obj: The Profile instance being serialized.

        Returns:
        - bool: True if the current user is the owner, False otherwise.
        """
        request = self.context['request']
        return request.user == obj.user

    def get_following_id(self, obj):
        """
        Custom method to retrieve the following relationship ID for the current user.

        Args:
        - obj: The Profile instance being serialized.

        Returns:
        - int or None: The following relationship ID if the current user is following the profile,
          or None otherwise.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                user=user, followed=obj.user
                ).first()
            return following.id if following else None
        return None

    class Meta:
        """
        Meta class for defining additional serializer-level properties.
        """
        model = Profile
        fields = [
            'id', 'user', 'created_at', 'modified_at', 'name',
            'bio', 'interests', 'image', 'is_user', 'following_id',
            'posts_count', 'followers_count', 'following_count',
        ]

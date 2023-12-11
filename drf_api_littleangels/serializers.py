from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer class for representing the current user's details.
    This serializer extends UserDetailsSerializer and adds additional fields for user profile details.
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        """
        - fields: List of fields to be included in the serialized output, extending the fields from UserDetailsSerializer.
        """
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
            )

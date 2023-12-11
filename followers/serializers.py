from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Follower model, providing a way to convert
    Follower instances to and from JSON format.
    """
    user = serializers.ReadOnlyField(source='user.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        """
        Meta class for defining additional serializer-level properties.
        """
        model = Follower
        fields = [
            'id', 'user', 'created_at', 'followed', 'followed_name',
        ]

    def create(self, validate_data):
        """
        Custom create method to handle the creation of Follower instances.

        Args:
        - validate_data: The validated data from the serialized input.

        Returns:
        - Follower: The created Follower instance.

        Raises:
        - serializers.ValidationError: If there is an IntegrityError,
        indicating a possible duplicate.
        """
        try:
            return super().create(validate_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail:' 'possible duplicate'
                })

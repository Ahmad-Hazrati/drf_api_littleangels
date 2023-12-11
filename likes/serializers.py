from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Like model, providing a way to convert
    Like instances to and from JSON format.
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        """
        Meta class for defining additional serializer-level properties.
        """
        model = Like
        fields = [
            'id', 'created_at', 'user', 'post',
        ]

    def create(self, validate_data):
        """
        Custom create method to handle the creation of Like instances.

        Args:
        - validate_data: The validated data from the serialized input.

        Returns:
        - Like: The created Like instance.

        Raises:
        - serializers.ValidationError: If there is an IntegrityError,
        indicating a possible duplicate.
        """
        try:
            return super().create(validate_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
                })

from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Booking model.

    This serializer is used to convert Booking model instances into JSON representations
    for API responses and to validate and parse incoming data for creating or updating Booking instances.
    """
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')

    class Meta:
        model = Booking
        fields = [
            'id', 'created_at', 'modified_at', 'event',
            'profile_id', 'profile_image',
        ]

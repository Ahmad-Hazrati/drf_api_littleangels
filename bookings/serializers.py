from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')

    class Meta:
        model = Booking
        fields = [
            'id', 'created_at', 'modified_at', 'event',
            'profile_id', 'profile_image',
        ]

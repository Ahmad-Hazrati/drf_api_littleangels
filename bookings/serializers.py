from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    # is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')
    # created_at = serializers.SerializerMethodField()
    # modified_at = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = [
            'id', 'created_at', 'modified_at', 'event',
            'profile_id', 'profile_image',
        ]

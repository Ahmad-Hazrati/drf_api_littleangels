from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Booking model.

    This serializer is used to convert Booking model instances
    into JSON representations for API responses and to validate
    and parse incoming data for creating or updating Booking instances.
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')
    created_at = serializers.SerializerMethodField()
    modified_at = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        """
        Method to determine if the current request user is
        the creator of the booking.
        """
        request = self.context['request']
        return request.user == obj.user

    def get_created_at(self, obj):
        """
        Method to return a human-readable time difference
        since the booking was created.
        """
        return naturaltime(obj.created_at)

    def get_modified_at(self, obj):
        """
        Method to return a human-readable time difference
        since the booking was last modified.
        """
        return naturaltime(obj.modified_at)

    class Meta:
        model = Booking
        fields = [
            'id', 'user', 'is_user', 'created_at', 'modified_at', 'event',
            'profile_id', 'profile_image',
        ]

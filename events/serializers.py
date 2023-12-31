from rest_framework import serializers
from .models import Category, Event
from bookings.models import Booking


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """
    class Meta:
        model = Category
        fields = (
            'id', 'title',
        )


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Event model.
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')
    booking_id = serializers.SerializerMethodField()
    bookings_count = serializers.ReadOnlyField()

    def get_is_user(self, obj):
        """
        Custom method to determine if the current user
        is the author of the post.

        Args:
        - obj: The Post instance being serialized.

        Returns:
        - bool: True if the current user is the author, False otherwise.
        """
        request = self.context['request']
        return request.user == obj.user

    def get_booking_id(self, obj):
        """
        Retrieves the ID of the booking associated with the event for
        the authenticated user.

        Parameters:
        - obj (Event): The Event object being serialized.

        Returns:
        - int or None: The ID of the booking associated with the event for
        the authenticated user or None if not found.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            booking = Booking.objects.filter(
                user=user, event=obj
            ).first()
            return booking.id if booking else None
        return None

    class Meta:
        model = Event
        fields = (
            'id', 'user', 'is_user', 'profile_id', 'profile_image', 'title',
            'description', 'event_image', 'image_filter', 'alt_tag',
            'venue', 'published', 'status', 'eventobjects',
            'start_date', 'end_date', 'created_at', 'modified_at',
            'booking_id', 'bookings_count',
        )

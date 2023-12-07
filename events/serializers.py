from rest_framework import serializers
from .models import Category, Event
from bookings.models import Booking


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'title',
        )


class EventSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    # is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')
    booking_id = serializers.SerializerMethodField()
    bookings_count = serializers.ReadOnlyField()
    

    # def get_is_user(self, obj):
    #     request = self.context['request']
    #     return request.user == obj.user

    def get_booking_id(self, obj):
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
            'id', 'profile_id', 'profile_image', 'title',
            'description', 'event_image','image_filter', 'alt_tag',
            'venue', 'published', 'status', 'eventobjects', 
            'start_date', 'end_date',
            'created_at', 'modified_at','booking_id', 'bookings_count',
        )

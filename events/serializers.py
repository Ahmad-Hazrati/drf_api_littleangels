from rest_framework import serializers
from .models import Category, Event
# from likes.models import Like


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
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    # def get_is_user(self, obj):
    #     request = self.context['request']
    #     return request.user == obj.user

    # def get_like_id(self, obj):
    #     user = self.context['request'].user
    #     if user.is_authenticated:
    #         like = Like.objects.filter(
    #             user=user, post=obj
    #         ).first()
    #         return like.id if like else None
    #     return None

    class Meta:
        model = Event
        fields = (
            'id', 'profile_id', 'profile_image', 'title', 'excerpt', 
            'description', 'event_image','image_filter', 'alt_tag',
            'venue', 'published', 'status', 'eventobjects', 'max_seats', 
            'registered_seats', 'available_seats', 'start_date', 'end_date',
            'created_at', 'modified_at', 'likes_count', 'comments_count',
        )

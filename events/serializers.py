from rest_framework import serializers
from .models import Category, Event
from likes.models import Like


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'title',
        )


class EventSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                user=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Event
        fields = (
            'id', 'user', 'is_user', 'category', 'title', 'excerpt', 'description',
            'venue', 'slug', 'published', 'status',
            'max_guests', 'guests_registered', 'start_date', 'end_date',
            'created_at', 'modified_at', 'like_id', 'likes_count',
        )

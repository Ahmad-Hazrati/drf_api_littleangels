from rest_framework import serializers
from .models import Category, Event


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'title',
        )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id', 'category', 'title', 'excerpt', 'description',
            'venue', 'slug', 'published', 'author', 'status',
            'max_guests', 'guests_registered', 'start_date', 'end_date',
            'created_at', 'modified_at',
        )

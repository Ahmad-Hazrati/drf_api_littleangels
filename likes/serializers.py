from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields = [
            'id', 'created_at', 'user', 'post',
        ]

    def create(self, validate_data):
        try:
            return super().create(validate_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
                })

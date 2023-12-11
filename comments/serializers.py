from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Comment model.
    This serializer is used to convert Comment model instances into JSON representations
    for API responses and to validate and parse incoming data for creating or updating Comment instances.
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')
    created_at = serializers.SerializerMethodField()
    modified_at = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        """
        Method to determine if the current request user is the creator of the comment.
        """
        request = self.context['request']
        return request.user == obj.user

    def get_created_at(self, obj):
        """
        Method to return a human-readable time difference since the comment was created.
        """
        return naturaltime(obj.created_at)

    def get_modified_at(self, obj):
        """
        Method to return a human-readable time difference since the comment was last modified.
        """
        return naturaltime(obj.modified_at)

    class Meta:
        model = Comment
        fields = [
            'id', 'user', 'is_user', 'profile_id', 'profile_image',
            'post', 'created_at', 'modified_at', 'description',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer class for detailed representation of Comment instances.
    This serializer extends the CommentSerializer and includes additional details for the associated post.
    """
    post = serializers.ReadOnlyField(source='post.id')

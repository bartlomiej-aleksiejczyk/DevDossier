from rest_framework import serializers

from tracker.models import Tag, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

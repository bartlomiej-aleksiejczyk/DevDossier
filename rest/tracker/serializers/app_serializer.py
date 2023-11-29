from rest_framework import serializers
from tracker.models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'
        read_only_fields = ['createdBy']
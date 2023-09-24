from rest_framework import serializers
from django.utils import timezone

from fileApp.models import File


class FileSerializer(serializers.Serializer):

    file = serializers.FileField()
    uploaded_at = serializers.DateTimeField(read_only=True, default=timezone.now)
    proceesed = serializers.BooleanField(default = False)

	    
    def create(self, validated_data):
        return File.objects.create(**validated_data)
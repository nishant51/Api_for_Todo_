from rest_framework import serializers
from .models import task

class taskserializers(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = (
            "id",
            "title",
            "complete",
        )
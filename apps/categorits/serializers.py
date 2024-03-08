from rest_framework import serializers

from apps.categorits.models import Categorits

class CategoritsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorits
        fields = ('id', 'title', 'parent', 'slug')
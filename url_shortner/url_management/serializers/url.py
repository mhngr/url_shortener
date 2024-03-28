from rest_framework import serializers
from ..models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'


class UrlSerializerV2(UrlSerializer):
    class Meta:
        model = Url
        fields = ['short_url', 'name', 'category']

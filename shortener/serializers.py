from rest_framework.serializers import ModelSerializer
from shortener.models import URLItem


class URLItemCreateSerializer(ModelSerializer):
    
    class Meta:
        model = URLItem
        fields = ('url',)


class URLItemListSerializer(ModelSerializer):
    
    class Meta:
        model = URLItem
        fields = ('url', 'reference')
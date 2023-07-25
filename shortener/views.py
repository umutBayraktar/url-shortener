import hashlib
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shortener.models import URLItem
from shortener.serializers import URLItemCreateSerializer, URLItemListSerializer
from shortener.utils import get_md5_hash
from django.shortcuts import redirect
from django.urls import reverse
from django.core.cache import cache

class HashURLAPIView(APIView):
    http_method_names = ["post"]
    def post(self, request, format=None):
        serializer = URLItemCreateSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            try:
                hash_value = get_md5_hash(url)
                cached_item = cache.get(hash_value)
                if cached_item:
                    return Response({"short": reverse('shortener:redirect_to_hashed_url', kwargs={'hashed_url': hash_value})}, status=status.HTTP_200_OK)
                url_item, created = URLItem.objects.get_or_create(reference=hash_value, url=url)
                return_url = reverse('shortener:redirect_to_hashed_url', kwargs={'hashed_url': url_item.reference})
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            if created:
                return Response({"short": return_url}, status=status.HTTP_201_CREATED)
            return Response({"short": return_url}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedirectToHashedURL(APIView):
    def get(self, request, hashed_url, format=None):
        try:
            cached_item = cache.get(hashed_url)
            if cached_item:
                return redirect(cached_item)
            url_obj = URLItem.objects.get(reference=hashed_url)
            cache.set(url_obj.reference, url_obj.url)
            return redirect(url_obj.url)
        except URLItem.DoesNotExist:
            return Response({'error': 'Hashed URL not found.'}, status=status.HTTP_404_NOT_FOUND)
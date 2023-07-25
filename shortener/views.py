import hashlib
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shortener.models import URLItem
from shortener.serializers import URLItemCreateSerializer, URLItemListSerializer
from shortener.utils import get_md5_hash
from django.shortcuts import redirect
from django.urls import reverse

class HashURLAPIView(APIView):
    def post(self, request, format=None):
        serializer = URLItemCreateSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            hash_value = get_md5_hash(url)
            import pdb;pdb.set_trace()
            url_item = URLItem.objects.get(reference=hash_value)
            if url_item:
                return_url = reverse('shortener:redirect_to_hashed_url', kwargs={'hashed_url': url_item.reference})
                return Response({'hashed_url': return_url}, status=status.HTTP_200_OK)
            url_item = URLItem.objects.create(reference=hash_value, url=url)
            return Response({'hashed_url': url_item.reference}, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        urls = URLItem.objects.all()
        serializer = URLItemListSerializer(urls, many=True)
        return Response(serializer.data)


class RedirectToHashedURL(APIView):
    def get(self, request, hashed_url, format=None):
        try:
            url_obj = URLItem.objects.get(reference=hashed_url)
            return redirect(url_obj.url)
        except URLItem.DoesNotExist:
            return Response({'error': 'Hashed URL not found.'}, status=status.HTTP_404_NOT_FOUND)
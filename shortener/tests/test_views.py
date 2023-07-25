from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from shortener.models import URLItem
from shortener.utils import get_md5_hash

class HashURLAPIViewTestCase(APITestCase):
    def test_create_hashed_url(self):
        url = "https://example.com"
        hash_value = get_md5_hash(url)
        data = {'url': url}
        expected_url = reverse('shortener:redirect_to_hashed_url', kwargs={'hashed_url':hash_value})
        response = self.client.post(reverse('shortener:hash_url_api'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('short', response.data)
        self.assertEqual(response.data["short"], expected_url)
        self.assertTrue(URLItem.objects.filter(reference=hash_value).exists())

    def test_duplicate_url(self):
        url = "https://example.com"
        hash_value = get_md5_hash(url)
        URLItem.objects.create(reference=hash_value, url=url)
        data = {'url': url}
        expected_url = reverse('shortener:redirect_to_hashed_url', kwargs={'hashed_url':hash_value})
        response = self.client.post(reverse('shortener:hash_url_api'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('short', response.data)
        self.assertEqual(response.data["short"], expected_url)
        self.assertEqual(URLItem.objects.filter(reference=hash_value).count(), 1)

    def test_invalid_url(self):
        data = {'url': 'invalid_url'}
        response = self.client.post(reverse('shortener:hash_url_api'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_url_integer(self):
        data = {'url': '1215'}
        response = self.client.post(reverse('shortener:hash_url_api'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_method(self):
        url = "https://example.com"
        data = {'url': url}
        response = self.client.get(reverse('shortener:hash_url_api'))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

class RedirectToHashedURLTestCase(APITestCase):
    def test_redirect_valid_hashed_url(self):
        url = "https://example.com"
        hashed_url = get_md5_hash(url)
        URLItem.objects.create(reference=hashed_url, url=url)
        response = self.client.get(reverse('shortener:redirect_to_hashed_url', kwargs={'hashed_url': hashed_url}))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.url, url)

    def test_redirect_invalid_hashed_url(self):
        hashed_url = 'invalid_hashed_url'
        response = self.client.get(reverse('shortener:redirect_to_hashed_url', kwargs={'hashed_url': hashed_url}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

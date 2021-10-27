from django.http import response
from django.test.utils import Approximate
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User


class PostTests(APITestCase):
    """
    test if we can make a post with our api.
    """
    def test_view_posts(self):
        # bringing back the url for listcreate :
        url = reverse('blog_api:listcreate') #= 127.0.0/api/
        # client to fake a browser, check the response. we are looking for response = 200
        response = self.client.get(url, fromat='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        self.test_category = Category.objects.create(name='django')

        self.testuser1 = User.objects.create_user(username='test_user1', password='123456789')

        data = {"title": "new", "author": 1, "excerpt": "new", "content": "new"}
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
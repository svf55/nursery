import os
from rest_framework import status
from rest_framework.test import APITestCase
from django.conf import settings
from child.models import Child


class TestChild(APITestCase):

    def test_create_child(self):
        """
        Ensure we can create a new Child object.
        """
        with open(os.path.join(settings.MEDIA_ROOT, 'images/test.jpg'), 'rb') as image:
            data = {
                'name': 'test1',
                'sex': 'M',
                'image': image
            }
            response = self.client.post('/api/v1/children/', data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Child.objects.count(), 1)
        self.assertEqual(Child.objects.get().name, 'test1')
        self.assertEqual(Child.objects.get().sex, 'M')
        self.assertIsNotNone(Child.objects.get().image)


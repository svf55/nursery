from rest_framework import status
from rest_framework.test import APITestCase
from journal.models import Journal


class TestJournal(APITestCase):

    fixtures = ['journal.json']

    def test_filtration(self):
        response = self.client.get('/api/v1/journals/?child__is_studying=True', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

        response = self.client.get('/api/v1/journals/?child__is_studying=False', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_journal(self):
        """
        Ensure we can create a new Journal object.
        """
        count_before = Journal.objects.count()
        data = {
            'child': 1
        }
        response = self.client.post('/api/v1/journals/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Journal.objects.count(), count_before + 1)

    def test_update_journal(self):
        """
        Ensure we can create a new Journal object.
        """
        data = {
            'id': 5,
            'led_parent': 'F'
        }
        response = self.client.patch('/api/v1/journals/5/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


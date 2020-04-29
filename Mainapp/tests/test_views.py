from django.test import TestCase, Client
from django.urls import reverse
from Mainapp.models import Diary
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index = reverse('index')

    def test_diary_index_GET(self):

        response = self.client.get(self.index)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Mainapp2/index.html')

    # def test_diary_POST(self):

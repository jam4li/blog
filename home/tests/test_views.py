from django.test import TestCase
from django.urls import reverse


class AdminViewTest(TestCase):
    def test_admin_response(self):
        url = reverse('admin:login')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

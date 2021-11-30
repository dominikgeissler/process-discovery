from django.test import TestCase
from django.urls import reverse

class AboutViewTests(TestCase):
    def test_get(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is the about page.")


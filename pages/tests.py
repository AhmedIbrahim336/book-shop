from django.test import TestCase

# user simpleTestCase to test webpages 
from django.test import SimpleTestCase
from django.urls.base import reverse

class HomepageTests(SimpleTestCase):
    # test the url 
    def test_homepage_status_code(slef):
        # test the home page
        response = slef.client.get('/')
        slef.assertEqual(response.status_code, 200)
    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_homepage_template(self):
        response = self.client.get('/') 
        self.assertTemplateUsed(response, 'home.html')

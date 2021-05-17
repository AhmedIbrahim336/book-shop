from pages.views import homePageView
from django.test import TestCase

# user simpleTestCase to test webpages 
from django.test import SimpleTestCase
from django.urls.base import resolve, reverse

class HomepageTests(SimpleTestCase):

    # Dont' repeat your self -> get the response and store it in a property in the self class 
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get('/')

    # test the url 
    def test_homepage_status_code(self):
        # test the home page
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code,200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_html(self):
        self.assertContains( self.response, 'Homepage')

    def test_homepage_not_contain_html(self):
        self.assertNotContains(self.response , 'Hi, there I should not be on the page')
    # test the view name 
    def test_hompage_url_resolvers_homepageView(self):
        view = resolve('/')

        self.assertEqual(
            view.func.__name__ ,
            homePageView.as_view().__name__
        )
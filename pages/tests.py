from pages.views import homePageView, AboutPageView
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

class AboutPageTest(SimpleTestCase):
    def setUp(self):
        # reverse the url
        url = reverse('about')
        # get the url response 
        self.response = self.client.get(url)
        # Take a look 
        print(self.response)
    
    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code , 200)
    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')
    def test_aboutpage_does_not_contain_incorrect_html(slef):
        slef.assertNotContains(slef.response, 'Hi, there! I should not be on the page')
    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/about')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
        

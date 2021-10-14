from django.test import SimpleTestCase
from django.urls import resolve, reverse
from HomePage.views import *

class TestUrls(SimpleTestCase):

    def testLoginPage(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func, index)
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from loginPage.views import *

class TestUrls(SimpleTestCase):

    def testLoginPage(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func, index)
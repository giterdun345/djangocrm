from django.test import TestCase
from django.shortcuts import reverse

class LandingPageTest(TestCase):
# id you start the method off with test_ it will execute as a single test 
  def test_status_code(self):
    response = self.client.get(reverse('landing-page'))
    # client a way to send requests
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "landing.html")
    # print(response.status_code)

# in order to run tests use manage.py test
# optimally use one test instead of multiple for optimization
# by default django will find the tests folder and run the tests accordingly 
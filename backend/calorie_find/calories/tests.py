from django.test import TestCase
from rest_framework.test import APIRequestFactory
from calories.models import Food

# Create your tests here.
class RestTest(TestCase):

    def setUp(self):
        Food(name='pizza', calories=10.0)


    def test_single_item_one_match(self):
        factory = APIRequestFactory()
        data =  {
                "foods": ['pizza']
                }
        request = factory.get('/calories/', data)
        self.assertTrue(request.status_code, 200)
        cheese = request.data['pizza']
        self.assertTrue(cheese)
        self.assertEquals(1, cheese)
        self.assertEquals(10.0, cheese[0])
        expected = {
                'pizza': 10.0
                }
        self.assertEquals(expected, request.data)





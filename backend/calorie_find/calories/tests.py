import logging
import json

from django.test import TestCase
from rest_framework.test import APIRequestFactory
from calories.models import Food
from calories.views import CalorieView


# Create your tests here.
class RestTest(TestCase):

    def setUp(self):
        food = Food(name='pizza', calories=10.0)
        food.save()
        food = Food(name='icecream', calories=-1)
        food.save()
        food = Food(name='nonfat icecream', calories=12.0)
        food.save()


    def test_single_item_one_match(self):
        factory = APIRequestFactory()
        view = CalorieView.as_view()
        data =  {
                "foods": ['pizza']
                }
        request = factory.post('/api/v1/calories/', data, format='json')
        response = view(request, data)
        self.assertTrue(response.status_code, 200)
        logging.debug('Food found %s' % response.data)
        cheese = json.loads(response.data)['foods']
        self.assertTrue(cheese)
        self.assertEquals(1, len(cheese))
        self.assertEquals(10.0, cheese[0][0]['calories'])





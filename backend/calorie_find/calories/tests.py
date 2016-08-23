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

    def _response(self, food_list):
        factory = APIRequestFactory()
        view = CalorieView.as_view()
        data =  {
                "foods": [food_list]
                }
        request = factory.post('/api/v1/calories/', data, format='json')
        response = view(request, data)
        self.assertTrue(response.status_code, 200)
        return json.loads(response.data)['foods']


    def test_finding_nothing(self):
        cheese = self._response(['lolnothing'])
        self.assertTrue(cheese)
        self.assertEquals(0, len(cheese[0]))

    def test_single_item_one_match(self):
        cheese = self._response(['pizza'])
        self.assertTrue(cheese)
        self.assertEquals(1, len(cheese[0]), msg="Size of %s" % cheese)
        self.assertEquals(10.0, cheese[0][0]['calories'])


    def test_multiple_match(self):
        icecreams = self._response('icecream')
        self.assertTrue(icecreams)
        self.assertEquals(2, len(icecreams[2]))
        self.asssertEquals(-1, icecreams[0][0]['calories'])
        self.asssertEquals(12.0, icecreams[0][1]['calories'])



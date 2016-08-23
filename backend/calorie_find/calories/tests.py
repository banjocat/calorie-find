import logging
import json

from django.test import TestCase
from rest_framework.test import APIRequestFactory
from calories.models import Food
from calories.views import CalorieView


# Create your tests here.
class RestTest(TestCase):

    @classmethod
    def setUpClass(cls):
        Food.create(name='pizza', calories=10.0)
        Food.create(name='icecream', calories=-1)
        Food.create(name='nonfat icecream', calories=12.0)
        Food.create(name='fudge', calories=100000)
        super(RestTest, cls).setUpClass()

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CalorieView.as_view()


    def _response(self, food_list):
        data =  {
                "foods": food_list
                }
        request = self.factory.post('/api/v1/calories/', data, format='json')
        response = self.view(request, data)
        self.assertTrue(response.status_code, 200)
        return json.loads(response.data)['foods']


    def test_finding_nothing(self):
        '''
        No match should return nothing
        '''
        cheese = self._response(['lolnothing'])
        self.assertTrue(cheese)
        self.assertEquals(0, len(cheese[0]))

    def test_single_item_one_match(self):
        '''
        Match one item from the database
        '''
        cheese = self._response(['pizza'])
        self.assertTrue(cheese)
        self.assertEquals(1, len(cheese[0]), msg="Size of %s" % cheese)
        self.assertEquals(10.0, cheese[0][0]['calories'])


    def test_multiple_match(self):
        '''
        Multiple match returns multiple items
        '''
        icecreams = self._response(['icecream'])
        self.assertTrue(icecreams)
        self.assertEquals(2, len(icecreams[0]), msg=icecreams)
        self.assertEquals(-1, icecreams[0][0]['calories'], msg=icecreams)
        self.assertEquals(12.0, icecreams[0][1]['calories'])


    def test_multiple_match_with_single(self):
        '''
        Test query that returns a multi match and single match
        '''
        matches = self._response(['pizza', 'icecream'])
        self.assertTrue(matches)
        self.assertEquals(1, len(matches[0]), msg=matches)
        self.assertEquals(2, len(matches[1]), msg=matches)
        self.assertEquals(-1, matches[1][0]['calories'], msg=matches)
        self.assertEquals(12.0, matches[1][1]['calories'])
        self.assertEquals(10.0, matches[0][0]['calories'])




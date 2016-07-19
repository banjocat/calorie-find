from django.test import TestCase
from rest_framework.test import APIRequestFactory

# Create your tests here.
class RestTest(TestCase):

    def test_single_item_one_match(self):
        factory = APIRequestFactory()
        data =  {
                "foods": ['CHEESE,PAST PROCESS,SWISS']
                }
        request = factory.get('/calories/', data)
        self.assertTrue(request.status_code, 200)
        cheese = request.data['CHEESE,PAST PROCESS,SWISS']
        self.assertTrue(cheese)
        self.assertEquals(1, cheese)
        self.assertEquals(334.0, cheese[0])
        expected = {
                'CHEESE,PAST PROCESS,SWISS': 334.0
                }
        self.assertEquals(expected, request.data)





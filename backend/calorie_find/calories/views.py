import logging

from rest_framework import serializers
from calories.models import Food
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer 
from django.http import Http404


# Create your views here.
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('pk', 'name', 'calories')
        model = Food


class FoodListSerializer(serializers.Serializer):
    foods = serializers.ListField(child=FoodSerializer(many=True))
    class Meta:
        fields = ('foods')



class CalorieView(APIView):
    '''
    Returns a list of food with calories
    '''
    def post(self, request, format='json'):
        '''
        ---
        parameters:
            - name: foods
              required: true
              description: An array of food to lookup for calories
              type: array
        responses:
            200:
                description: Lookup done
        '''
        logging.debug('Start of CalorieView')
        if not request or not request.data:
            raise Http404
        logging.debug('Sent: ' + str(request.data))
        food_querysets = {"foods": []}
        for food in request.data['foods']:
            q = Food.objects.filter(name__icontains=food)
            food_querysets['foods'].append(q)

        logging.debug("Querysets %s" % food_querysets)
        serializer = FoodListSerializer(food_querysets)
        logging.debug("Serializer data %s" %  serializer.data)
        json = JSONRenderer().render(serializer.data)
        logging.debug('Json %s' % json)
        logging.debug('End of CalorieView')
        return Response(json)



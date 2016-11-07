from rest_framework import views
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import Http404
from django.db.models import Q

from calories.serializers import FoodListSerializer, FoodRequestSerializer
from calories.models import Food


class CalorieView(views.APIView):

    def get_serializer(self,):
        serializer = FoodRequestSerializer()
        return serializer

    def post(self, request):
        '''
        Returns a list of food with calories
        '''
        if 'foods' not in request.data:
            raise Http404
        food_querysets = {"foods": []}
        for food in request.data.get('foods'):
            q = Q(name__icontains=food.upper()) | Q(name__fuzzy=food.upper())
            result = Food.objects.filter(q)[:5]
            food_querysets['foods'].append(result)
        serializer = FoodListSerializer(food_querysets)
        json = JSONRenderer().render(serializer.data)
        return Response(json)

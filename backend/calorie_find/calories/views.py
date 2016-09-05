
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
        if not request or not request.data:
            raise Http404
        food_querysets = {"foods": []}
        for food in request.data.get('foods'):
            q = Food.objects.filter(name__fuzzy=food.upper())
            food_querysets['foods'].append(q)

        serializer = FoodListSerializer(food_querysets)
        json = JSONRenderer().render(serializer.data)
        return Response(json)



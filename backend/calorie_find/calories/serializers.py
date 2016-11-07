from rest_framework import serializers
from calories.models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('pk', 'name', 'calories')
        model = Food


class FoodListSerializer(serializers.Serializer):
    foods = serializers.ListField(child=FoodSerializer(many=True))

    class Meta:
        fields = ('foods')


class FoodRequestSerializer(serializers.Serializer):
    '''
    Used for getting data
    '''
    foods = serializers.CharField()

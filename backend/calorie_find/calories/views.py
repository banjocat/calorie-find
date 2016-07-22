from django.shortcuts import render
from rest_framework import serializers
from calories.models import Food
from rest_framework import generics
from django.db.models import Q

# Create your views here.

class CalorieRequestSerializer(serializers.Serializer):
    foods = serializers.ListField(child=serializers.CharField())


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Food
        fields = ('pk', 'name', 'calories')


class CalorieView(generics.ListAPIView):
    def get_queryset(self):
        q = []
        for food in self.request.GET['foods']:
            q = q | Q(name=food)

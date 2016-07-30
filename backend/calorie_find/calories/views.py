from django.shortcuts import render
from rest_framework import serializers
from calories.models import Food
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q

# Create your views here.

class CalorieRequestSerializer(serializers.Serializer):
    foods = serializers.ListField(child=serializers.CharField())
    class Meta:
        fields = ('foods')




class CalorieView(generics.ListAPIView):
    def get(self, request):
        '''
        Accepts list of food for calorie look up
        '''
        serializer = CalorieRequestSerializer()
        return Response(serializer.data)

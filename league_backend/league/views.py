from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import League
from .serializers import LeagueSerializer

# Create your views here.
def getRoutes(request):
    return JsonResponse('Hello', safe=False)

@api_view(['GET'])
def getLeagues(request):
    leagues = League.objects.all()
    serializer = LeagueSerializer(leagues, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getLeague(request):
    return Response('league')
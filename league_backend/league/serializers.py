from rest_framework import serializers
# ADD user model
from .models import League

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fiels = '__all__'
from rest_framework import serializers
from hotel_finder.models import PerfectHotel, TopDestination


class PerfectHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfectHotel
        fields = ['star', 'img']

class TopDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopDestination
        fields = ['wifi', 'breakfast', 'balcony', 'bathroom',
                  'content', 'img', 'name', 'star', 'price',]

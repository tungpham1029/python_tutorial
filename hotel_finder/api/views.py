from rest_framework import status, views
from rest_framework.response import  Response
from rest_framework.decorators import api_view


from .serializers import PerfectHotelSerializer, TopDestinationSerializer
from hotel_finder.models import PerfectHotel, TopDestination
from accounts.models import Profile


class LocationView(views.APIView):
    def get(self, request):
        #do something with 'GET' method
        return Response("some data")

    def post(self, request):
        #do something with 'POST' method
        return Response("some data")


@api_view(['GET', ])
def api_detail_perfect_hotel_view(request, star):

    try:
        perfect_hotel = PerfectHotel.objects.get(star = star)
    except PerfectHotel.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PerfectHotelSerializer(perfect_hotel)
        return Response(serializer.data)


@api_view(['PUT', ])
def api_update_perfect_hotel_view(request, star):

    try:
        perfect_hotel = PerfectHotel.objects.get(star = star)
    except PerfectHotel.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = PerfectHotelSerializer(perfect_hotel, data = request.data )
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', ])
def api_delete_perfect_hotel_view(request, star):

    try:
        perfect_hotel = PerfectHotel.objects.get(star = star)
    except PerfectHotel.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        operation  = perfect_hotel.delete()
        data = {}
        if operation:
            data["success"] = "deleted successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)

@api_view(['POST', ])
def api_create_perfect_hotel_view(request, star):
    account = Profile.objects.get(pk=1)
    perfect_hotel = PerfectHotel(star=account)
    if request.method == "POST":
        serializer = PerfectHotelSerializer(perfect_hotel, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def api_detail_top_destination_view(request, name):
    try:
        top_destination = TopDestination.objects.get(name = name)
    except TopDestination.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TopDestinationSerializer(top_destination)
        return Response(serializer.data)

@api_view(['PUT', ])
def api_update_top_destination_view(request, name):
    try:
        top_destination = TopDestination.objects.get(name = name)
    except TopDestination.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TopDestinationSerializer(top_destination, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Successful Update!"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
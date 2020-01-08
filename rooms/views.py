from django.shortcuts import render
from .models import Room
from hotels.models import Hotel
# Create your views here.


def hotel_room_page(request):
    rooms = Room.objects.all()
    hotels = Hotel.objects.all()
    context = {
        "hotels": hotels,
        "rooms": rooms,
    }
    return render(request, 'hotel-room-page.html', context)


def hotel_room_page_special_offer(request):
    return render(request, 'hotel-room-page-special-offer.html')


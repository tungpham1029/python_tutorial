from django.shortcuts import render
from hotels.models import Hotel
from .models import RoomImage, Room

# Create your views here.


def booking(request, slug):
    hotel = Hotel.objects.get(slug=slug)
    room = Room.objects.filter(hotel=hotel)
    first_room = Room.objects.filter(hotel=hotel).first()
    context = {
        'first_room': first_room,
        'hotels': hotel,
        'rooms': room,
    }
    return render(request, 'booking.html', context)
from django.shortcuts import render
from .models import Hotel, HotelImage


# Create your views here.


def home(request):
    hotels = Hotel.objects.all()
    context = {
        'hotels': hotels
    }
    return render(request, 'home.html', context)


def detail_hotel(request, slug):
    hotels = Hotel.objects.get(slug=slug)
    slugs = Hotel.objects.filter(slug=slug)
    images = HotelImage.objects.filter(hotel=hotels)
    context = {
        'slugs': slugs,
        'hotels': hotels,
        'images': images,
    }
    return render(request, 'detail_hotel.html', context)


def payment(request):
    return render(request, 'payment.html')

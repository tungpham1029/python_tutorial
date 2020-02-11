from django.http import HttpResponse
from django.shortcuts import render, redirect
from hotels.models import Hotel, HotelImage
from .forms import PersonForm
from .models import Person

# Create your views here.


def payment(request, slug):
    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            form.save()
            print('done')
            return redirect('home')
        else:
            hotels = Hotel.objects.get(slug=slug)
            slugs = Hotel.objects.filter(slug=slug)
            images = HotelImage.objects.filter(hotel=hotels)
            context = {
                'slugs': slugs,
                'hotels': hotels,
                'images': images,
                'form': form,
            }
            return render(request, 'payment.html', context)
    else:
        form = PersonForm(None)
        hotels = Hotel.objects.get(slug=slug)
        slugs = Hotel.objects.filter(slug=slug)
        images = HotelImage.objects.filter(hotel=hotels)
        context = {
            'slugs': slugs,
            'hotels': hotels,
            'images': images,
            'form': form,
        }
        return render(request, 'payment.html', context)


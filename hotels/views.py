from django.shortcuts import render
from .models import Hotel
# Create your views here.


def hotel_page_v1(request):
    hotels = Hotel.objects.all()
    context = {
        "hotels": hotels,
    }
    return render(request, 'hotel-page-v1.html', context)


def hotel_page_v2(request):
    return render(request, 'hotel-page-v2.html')


def hotel_page_v3(request):
    return render(request, 'hotel-page-v3.html')


def hotel_page_v4(request):
    return render(request, 'hotel-page-v4.html')


def hotel_room_page(request):
    return render(request, 'hotel-room-page.html')


def hotel_room_page_special_offer(request):
    return render(request, 'hotel-room-page-special-offer.html')


def search_result(request):
    hotels = Hotel.objects.all()
    context = {
        "hotels": hotels,
    }
    return render(request, 'search-result.html', context)


def search_result_2(request):
    return render(request, 'search-result-2.html')


def search_result_3(request):
    return render(request, 'search-result-3.html')


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None

    if q:
        hotels = Hotel.objects.filter(title_icontains = q)
        context = {
            "hotels": hotels,
            "query": q
        }

    template = 'xxxx.html'
    return render(request, template, context)
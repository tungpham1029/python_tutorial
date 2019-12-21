from django.contrib import auth, messages
from django.shortcuts import render, redirect
from .models import PerfectHotel, TopDestination, USP, DiscoverTheWorld, VisitorExp


# Create your views here.


def index(request):
    perfect = PerfectHotel.objects.all()
    topdes = TopDestination.objects.all()
    usps = USP.objects.all()
    discovers = DiscoverTheWorld.objects.all()
    visitors = VisitorExp.objects.all()
    return render(request, 'index.html', {'perfs': perfect,
                                          'topdes' : topdes,
                                          'usps': usps,
                                          'discovers' : discovers,
                                          'visitors': visitors })

def elements(request):
    return render(request, 'elements.html')

def blog_index(request):
    return render(request, 'blog-index.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def about(request):
    return render(request, 'about-us.html')

def search_result(request):
    return render(request, 'search-result.html')

def search_result_2(request):
    return render(request, 'search-result-2.html')

def search_result_3(request):
    return render(request, 'search-result-3.html')

def hotel_page_v1(request):
    return render(request, 'hotel-page-v1.html')

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

def search_rooms(request):
    return render(request, 'search-rooms.html')

def contact_us(request):
    return render(request, 'contact-us.html')

def thanks_page(request):
    return render(request, 'thanks-page.html')

def page_404(request):
    return render(request, '404-page.html')

def payment(request):
    return render(request, 'payment.html')






























def test_index(request):
    return render(request, 'test_index.html')

def indexsta(request):
    return render(request, 'indexsta.html')
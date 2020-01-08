from django.urls import path
from . import views

urlpatterns = [
    path('hotel-room-page', views.hotel_room_page, name='hotel-room-page'),
    path('hotel-room-page-special-offer', views.hotel_room_page_special_offer, name='hotel-room-page-special-offer'),

]
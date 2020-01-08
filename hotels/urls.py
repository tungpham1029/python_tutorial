from django.urls import path
from . import views

urlpatterns = [
    path('hotel-page-v1', views.hotel_page_v1, name='hotel-page-v1'),
    path('hotel-page-v2', views.hotel_page_v2, name='hotel-page-v2'),
    path('hotel-page-v3', views.hotel_page_v3, name='hotel-page-v3'),
    path('hotel-page-v4', views.hotel_page_v4, name='hotel-page-v4'),
    path('hotel-room-page', views.hotel_room_page, name='hotel-room-page'),
    path('hotel-room-page-special-offer', views.hotel_room_page_special_offer, name='hotel-room-page-special-offer'),
    path('search-result', views.search_result, name='search-result'),
    path('search-result-2', views.search_result_2, name='search-result-2'),
    path('search-result-3', views.search_result_3, name='search-result-3'),
]
from django.urls import path
from .views import (
    api_detail_perfect_hotel_view,
    api_detail_top_destination_view,
    api_create_perfect_hotel_view,
    api_delete_perfect_hotel_view,
    api_update_perfect_hotel_view,
    api_update_top_destination_view,
)

app_name = 'perfect_hotel'

urlpatterns = [
    path('perfecthotel/<star>/', api_detail_perfect_hotel_view, name = 'perfect-hotel'),
    path('perfecthotel/<star>/update/', api_update_perfect_hotel_view, name = 'perfect-hotel-update'),
    path('perfecthotel/create/', api_create_perfect_hotel_view, name = 'perfect-hotel-create'),
    path('perfecthotel/<star>/delete/', api_delete_perfect_hotel_view, name = 'perfect-hotel-delete'),
    path('topdestination/<name>/', api_detail_top_destination_view, name = 'top-destination'),
    path('topdestination/<name>/update/', api_update_perfect_hotel_view, name = 'top-destination-update'),

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('test_index', views.test_index, name = 'test_index'),
    path('indexsta', views.indexsta, name = 'indexsta'),
    path('elements', views.elements, name = 'elements'),
    path('blog-index', views.blog_index, name = 'blog-index'),
    path('blog-single', views.blog_single, name='blog-single'),
    path('about-us', views.about, name = 'about-us'),
    path('search-result', views.search_result, name='search-result'),
    path('search-result-2', views.search_result_2, name='search-result-2'),
    path('search-result-3', views.search_result_3, name='search-result-3'),
    path('hotel-page-v1', views.hotel_page_v1, name='hotel-page-v1'),
    path('hotel-page-v2', views.hotel_page_v2, name='hotel-page-v2'),
    path('hotel-page-v3', views.hotel_page_v3, name='hotel-page-v3'),
    path('hotel-page-v4', views.hotel_page_v4, name='hotel-page-v4'),
    path('hotel-room-page', views.hotel_room_page, name='hotel-room-page'),
    path('hotel-room-page-special-offer', views.hotel_room_page_special_offer, name='hotel-room-page-special-offer'),
    path('search-rooms', views.search_rooms, name='search-rooms'),
    path('contact-us', views.contact_us, name='contact-us'),
    path('thanks-page', views.thanks_page, name='thanks-page'),
    path('404-page', views.page_404, name='404-page'),
    path('payment', views.payment, name = 'payment'),
]
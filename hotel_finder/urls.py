from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('elements', views.elements, name = 'elements'),
    path('blog-index', views.blog_index, name = 'blog-index'),
    path('blog-single', views.blog_single, name='blog-single'),
    path('about-us', views.about, name = 'about-us'),
    path('search-rooms', views.search_rooms, name='search-rooms'),
    path('contact-us', views.contact_us, name='contact-us'),
    path('thanks-page', views.thanks_page, name='thanks-page'),
    path('404-page', views.page_404, name='404-page'),
    path('payment', views.payment, name = 'payment'),
]
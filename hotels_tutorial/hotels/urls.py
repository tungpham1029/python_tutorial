from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail_hotel/<slug>/', views.detail_hotel, name='detail_hotel'),
    path('payment', views.payment, name='payment'),
]
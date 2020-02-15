from django.urls import path
from . import views

urlpatterns = [
    path('payment/<slug>', views.payment, name='payment'),
    path('thanks_page', views.thanks_page, name='thanks_page'),
]
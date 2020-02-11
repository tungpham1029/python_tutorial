from django.urls import path
from . import views

urlpatterns = [
    path('payment/<slug>', views.payment, name='payment'),
]
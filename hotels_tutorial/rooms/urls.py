from django.urls import path
from . import views

urlpatterns = [
    path('booking/<slug>/', views.booking, name='booking'),
]
from django.db import models

# Create your models here.
from django.urls import reverse


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    mail = models.EmailField()
    slug = models.SlugField(unique=True)
    star = models.IntegerField()
    safe_off = models.BooleanField(default=False)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail_hotel", kwargs={'slug': self.slug})


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotels/')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    activate = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.hotel.name
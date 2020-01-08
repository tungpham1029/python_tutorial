from django.db import models

# Create your models here.
from django.urls import reverse

STAR_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    mail = models.EmailField()
    price = models.DecimalField(decimal_places=2, max_digits=100, default=100)
    price_safe_off = models.DecimalField(decimal_places=2, max_digits=100, default=100)
    slug = models.SlugField(unique=True)
    star = models.IntegerField(choices=STAR_CHOICES, default=3)
    safe_off = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail_hotel", kwargs={'slug': self.slug})


class HotelImage(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='hotels/', default='hotel.png')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)

    def __str__(self):
        return self.hotel.name

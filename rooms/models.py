from django.db import models

# Create your models here.


OPTION_CHOICES = (
    ('1 single', '1 single bed in 1 room'),
    ('2 single', '2 single bed in 1 room'),
    ('1 double', '1 double bed in 1 room'),
    ('2 double', '2 double bed in 1 room'),
    ('4 single', '4 single bed in 1 room'),
    ('4 double', '4 double bed in 1 room'),
)


class Room(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=100)
    booked = models.BooleanField(default=False)
    option = models.CharField(max_length=100, choices=OPTION_CHOICES, default='1')
    safe_off = models.BooleanField(default=False)
    time_check_in = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    time_check_out = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.name


class RoomImage(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='rooms/')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.room.name

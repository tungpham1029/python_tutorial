from django.contrib import admin
from .models import RoomImage, Room

# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'booked', 'option', 'safe_off', 'time_check_in', 'time_check_out']
    list_editable = ['price', 'safe_off', 'time_check_in', 'time_check_out']

    class Meta:
        model = Room


admin.site.register(Room, RoomAdmin)
admin.site.register(RoomImage)
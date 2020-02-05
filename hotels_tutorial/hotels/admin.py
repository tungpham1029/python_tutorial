from django.contrib import admin
from .models import Hotel, HotelImage

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name", )}

    class Meta:
        model = Hotel


admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelImage)


from django.contrib import admin

from .models import Rooms

# Register your models here.
class RoomsAdmin(admin.ModelAdmin):
    

    list_display = ('room_number','room_type','capcity')
    list_editable = ('capcity','room_type')
    list_display_links= ('room_number',)
    list_filter = ('capcity', 'room_type')

   
    list_per_page = 25


admin.site.register(Rooms, RoomsAdmin)

from django.contrib import admin
from .models import Registration


# Register your models here.

@admin.register(Registration)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['name', 'college', 'email', 'mob', 'is_veg', 'accommodation', 'is_ieee_member',
                    'member_id', 't_shirt_size']
    list_display_links = list_display[:]
    list_filter = ['college', 'is_veg', 'accommodation', 'is_ieee_member', 't_shirt_size']

from django.contrib import admin
from .models import Option


class OptionAdmin(admin.ModelAdmin):
        list_display = ["option_name","option_value","created","updated"]
        # list_display = [field.name for field in Option._meta.fields] #show all fields

admin.site.register(Option, OptionAdmin)

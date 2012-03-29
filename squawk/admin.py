from django.contrib import admin
from models import Squawk

class SquawkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Squawk, SquawkAdmin)
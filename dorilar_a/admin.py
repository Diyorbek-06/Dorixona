from django.contrib import admin
from .models import Dori
# Register your models here.


class DoriAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomi', 'price', 'miqdori')
    search_fields = ('nomi', 'price', 'miqdori')
    list_filter = ('price','miqdori')

admin.site.register(Dori, DoriAdmin)
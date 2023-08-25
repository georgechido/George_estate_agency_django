from django.contrib import admin
from .models import Properties

class PropertiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'price', 'list_date')
    list_display_links = ('id', 'name')
    list_filter = ('agent_id',)
    search_fields =('name', 'location')
    list_per_page = 25

admin.site.register(Properties, PropertiesAdmin)
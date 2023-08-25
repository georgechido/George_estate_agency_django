from django.contrib import admin
from .models import MyMessages

class AdminMessages(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'pname', 'plocation', 'msg_date', 'agent_id')
    list_display_links = ('id', 'email')
    list_filter = ('agent_id',)
    search_fields =('agent_id', 'name')
    list_per_page = 25

admin.site.register(MyMessages, AdminMessages)

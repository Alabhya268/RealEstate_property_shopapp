from django.contrib import admin

from .models import Contacts
 
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name', 'listing', 'email', 'contact_date')
    search_fields = ('id', 'name', 'listing' , 'email')
    list_display_links = ('id', 'name')
    list_per_page = 25 
admin.site.register(Contacts, ContactsAdmin)    


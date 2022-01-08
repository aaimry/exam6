from django.contrib import admin

from guest_book.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'text']
    list_filter = ['name', 'status']
    search_fields = ['name', 'status']
    fields = ['name', 'email', 'text', 'create_date', 'update_date', 'status']


admin.site.register(GuestBook, GuestBookAdmin)
from django.contrib import admin

from guest_book.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'text', 'status']
    list_filter = ['create_date']
    search_fields = ['name', 'status']
    fields = ['name', 'email', 'text', 'status']


admin.site.register(GuestBook, GuestBookAdmin)
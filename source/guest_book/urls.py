from django.urls import path

from guest_book.views import guest_book_view, guest_book_add_view, guest_book_update_view, guest_book_delete_view

urlpatterns = [
    path('', guest_book_view, name='index'),
    path('add/', guest_book_add_view, name='guest_book_add'),
    path('guest/<int:pk>/update', guest_book_update_view, name='guest_book_update'),
    path('guest/<int:pk>/delete', guest_book_delete_view, name='guest_book_delete')
]

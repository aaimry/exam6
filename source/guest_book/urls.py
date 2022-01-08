from django.urls import path

urlpatterns = [
    path('', guest_book_view, name='index'),
]
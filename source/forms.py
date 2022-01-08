from django import forms

from guest_book.models import STATUS_CHOICES, GuestBook


class GuestBookForm(forms.Form):
    name = forms.CharField(max_length=40, required=True, label='Имя')
    email = forms.EmailField(required=True, label='Email')
    text = forms.CharField(max_length=2000, required=True, label='Текст', widget=forms.Textarea())
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Статус',
                               initial=STATUS_CHOICES[0][1])


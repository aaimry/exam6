from django.shortcuts import render, redirect, get_object_or_404

from forms import GuestBookForm
from guest_book.models import GuestBook


def guest_book_view(request):
    guestbook = GuestBook.objects.all()
    return render(request, 'guestbook.html', {'guestbook': guestbook})


def guest_book_add_view(request):
    if request.method == 'GET':
        form = GuestBookForm()
        return render(request, 'guestbook_add.html', {'form': form})
    else:
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('text')
            create_date = form.cleaned_data.get('create_date')
            update_date = form.cleaned_data.get('update_date')
            status = form.cleaned_data.get('status')
            new_guest_book = GuestBook.objects.create(name=name, email=email, text=text,
                                                      create_date=create_date,
                                                      update_date=update_date,
                                                      status=status)
            new_guest_book.save()
            return redirect('index')
    return render(request, 'guestbook_add.html', {'form': form})


def guest_book_update_view(request, pk):
    guestbook = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        form = GuestBookForm(initial={
            'name': guestbook.name,
            'email': guestbook.email,
            'text': guestbook.text,
            'create_date': guestbook.create_date,
            'update_date': guestbook.update_date,
            'status': guestbook.status
        })
        return render(request, 'guestbook_update.html', {'guestbook': guestbook, 'form': form})
    else:
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            guestbook.name = form.cleaned_data.get('name')
            guestbook.email = form.cleaned_data.get('email')
            guestbook.text = form.cleaned_data.get('text')
            guestbook.create_date = form.cleaned_data.get('create_date')
            guestbook.update_date = form.cleaned_data.get('update_date')
            guestbook.status = form.cleaned_data.get('status')
            guestbook.save()
            return redirect('index')
        return render(request, 'guestbook_update.html', {'guestbook': guestbook, 'form': form})


def guest_book_delete_view(request, pk):
    guestbook = GuestBook.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'guestbook_delete.html', {'guestbook': guestbook})
    else:
        guestbook.delete()
        return redirect('index')

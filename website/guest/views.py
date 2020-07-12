from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import GuestForm
from .models import Guest

def index(request):
    status = ''
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = GuestForm()
        return render(request, 'guest/index.html', {'form': form, 'guests': Guest.objects.all(), 'status': status})

def edit(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    status = 'success'
    nameValue = Guest.objects.filter(pk=pk).values('name')[0]
    guest_name = nameValue['name']

    if request.method == 'POST':
        post_form = GuestForm(request.POST, instance=guest)
        if post_form.is_valid():
            post_form.save()
            return render(request, 'guest/edit.html', {'form': post_form, 'status': status, 'guest_name': guest_name})
    else:
        form = GuestForm(instance=guest)
        return render(request, 'guest/edit.html', {'form': form, 'guest_name': guest_name})

def delete(request, pk):
    guest = Guest.objects.get(pk=pk)
    guest.delete()
    return HttpResponseRedirect('/')

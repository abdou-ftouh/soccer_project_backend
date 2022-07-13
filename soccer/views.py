from django.shortcuts import render

# Create your views here.
from .models import Location, User
from django.shortcuts import render, redirect
from .forms import UserForm


def user_delete(request, pk):
    User.objects.get(id=pk).delete()
    return redirect('user_list')

def user_edit(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'soccer/user_form.html', {'form': form})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'soccer/user_form.html', {'form': form})


def user_list(request):
    users = User.objects.all()
    return render(request, 'soccer/user_list.html', {'users': users})

def location_list(request):
    locations = Location.objects.all()
    return render(request, 'soccer/location_list.html', {'locations': locations})

def user_detail(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'soccer/user_detail.html', {'user': user})
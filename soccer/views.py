
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, permissions


# Create your views here.

from .models import Location, Reservation, Stadium, User
from django.shortcuts import render, redirect
from .forms import UserForm



from rest_framework import generics 
from .serializers import UserSerializer, LocationSerializer, ReservationSerializer, StadiumSerializer


# def location_detail(request, pk):
#         location = Location.objects.get(id=pk)
#         print(location.city)
        
 


# def location_detail(request, pk):
#     location = Location.objects.get(id=pk)
#     print(location)
#     return JsonResponse(location)

def reservation_list(request):
    reservations = Reservation.objects.all()
    reservations_values=reservations.values('user','stadium','reserved_start_date','reserved_end_date',)
    list_reservations=list(reservations_values)
    return JsonResponse(list_reservations, safe=False)



def stadium_list(request):
    stadiums = Stadium.objects.all()
    stadiums_values=stadiums.values('location','name','photo','address','zip')
    list_stadiums=list(stadiums_values)
    return JsonResponse(list_stadiums, safe=False)


# def stadium_detail(request, pk):
#     stadium = Stadium.objects.get(id=pk)
#     print(stadium)
#     return 'ok'
    

# def reservation_delete(request, pk):
#     print(Reservation.objects.all())
#     # Reservation.objects.get(id=pk).delete()
#     return 'Ok'

# def reservation_create(request):
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             reservation = form.save()
#             return redirect('reservation_detail', pk=reservation.pk)
#     else:
#         form = ReservationForm()
#     return render(request, 'soccer/reservation_form.html', {'form': form})


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



def mock_login(request):
    return JsonResponse({'loggedIn':True, 'username': 'mock_user'})

def mock_signup(request):
    return JsonResponse({'loggedIn':True, 'username': 'mock_user'})


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]



class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]



class StadiumList(generics.ListCreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [permissions.AllowAny]

class StadiumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [permissions.AllowAny]



class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.AllowAny]

    # def post(self, request, *args, **kwargs):
    #     request.data['user_string'] = request.user.username
    #     return super().post(request, *args, **kwargs)

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
    permission_classes = [permissions.AllowAny]


class ReservationUpdateProtected(generics.UpdateAPIView):
    serializer_class = ReservationSerializer
    queryset  = Reservation.objects.all()

    permission_classes = [permissions.IsAdminUser]


class ReservationProtected(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer
    queryset  = Reservation.objects.all()

    permission_classes = [permissions.AllowAny]


# class ReservationList(generics.ListCreateAPIView):
#     queryset = Reservation.objects.all()
#     serializer_class = ReservationSerializer

# class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Reservation.objects.all()
#     serializer_class = ReservationSerializer






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
    return 'ok'
 

def user_list(request):
    users = User.objects.all()
    users_values=users.values('first_name','last_name','email')
    list_users=list(users_values)
    
    print(type(users))
    print(type(users_values))
    print(type(list_users))
    # users=users.order_by('first_name')
    # print(users)
    # return render(request, 'soccer/user_list.html', {'users': users})
    return JsonResponse(list_users, safe=False)

def location_list(request):
    locations = Location.objects.all()
    return render(request, 'soccer/location_list.html', {'locations': locations})

def user_detail(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'soccer/user_detail.html', {'user': user})
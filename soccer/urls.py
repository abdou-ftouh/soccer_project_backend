from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),


    path('locations/', views.LocationList.as_view(), name='location_list'),
    path('locations/<int:pk>', views.LocationDetail.as_view(), name='location-detail'),


    path('stadiums/', views.StadiumList.as_view(), name='stadium_list'),
    path('stadiums/<int:pk>', views.StadiumDetail.as_view(), name='stadium-detail'),

    path('reservations/', views.ReservationList.as_view(), name='reservation_list'),
    path('reservations/<int:pk>', views.ReservationDetail.as_view(), name='reservation_detail'),
    path('reservations/<int:pk>/edit', views.ReservationUpdateProtected.as_view()),


 


    # path('locations/<int:pk>', views.location_detail),
    # path('users/', views.user_list, name='user_list'),
    # path('locations/', views.location_list, name='location_list'),
    # path('users/<int:pk>', views.user_detail, name='user_detail'),
    # path('reservations/<int:pk>/delete', views.reservation_delete, name='reservation_delete'),
    # path('reservations/<int:pk>', views.reservation_detail, name='reservation_detail'),
    # path('reservations/new', views.reservation_create, name='reservation_create'),
    # path('reservations/<int:pk>/edit', views.reservation_edit, name='reservation_edit'),


    # path('reservations/', views.reservation_list, name='reservation_list'),
    # path('reservations/<int:pk>/delete', views.reservation_delete, name='reservation_delete'),


    # path('stadiums/', views.stadium_list),
    # path('stadiums/<int:pk>', views.stadium_detail),

    # path('users/new', views.user_create, name='user_create'),
    # path('users/<int:pk>/edit', views.user_edit, name='user_edit'),
    # path('users/<int:pk>/delete', views.user_delete, name='user_delete'),
]
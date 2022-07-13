from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('locations/', views.location_list, name='location_list'),
    path('users/<int:pk>', views.user_detail, name='user_detail'),
    path('users/new', views.user_create, name='user_create'),
    path('users/<int:pk>/edit', views.user_edit, name='user_edit'),
    path('users/<int:pk>/delete', views.user_delete, name='user_delete'),
]
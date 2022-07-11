from django.contrib import admin
from .models import User,Location,Reservation,Stadium
# Register your models here.
admin.site.register(User)
admin.site.register(Location)
admin.site.register(Reservation)
admin.site.register(Stadium)
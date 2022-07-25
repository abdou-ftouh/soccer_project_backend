from django import forms
from .models import User, Location

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','phone', 'gendre',)



class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ('city',)

# , 'address', 'zip',
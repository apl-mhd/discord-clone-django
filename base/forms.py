from django.forms import ModelForm, fields
from . models import Room
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'perticipants']



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

        
      
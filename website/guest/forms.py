from django.forms import ModelForm
from .models import Guest

class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'group', 'email', 'address', 'priority', 'inviter', 'estimate']
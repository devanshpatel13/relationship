from .models import *
from django import forms


class hotelform(forms.ModelForm):
    class Meta:
        model = hotel
        fields = ["pizza", "palce", "burger"]


class palceform(forms.ModelForm):
    class Meta:
        model = palce
        fields = ["name", "address"]


class waiterform(forms.ModelForm):
    class Meta:
        model = waiter
        fields = ["hotel", "name"]

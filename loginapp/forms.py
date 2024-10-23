from django import forms 
from .models import Shop,Booking
class Shopform(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ["shopname","owner","location","address","phoneno","openingtime","closingtime"]
class Bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name","loginid","bookingdate","bookingtime","products","deliverystatus"]
class Bookingeditform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["deliverystatus"]
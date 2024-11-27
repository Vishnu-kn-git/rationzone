from django import forms 
from .models import *
class Stockform(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["product","price","quantity"]

class Supplycostockform(forms.ModelForm):
    class Meta:
        model = Supplycostock
        fields = ["product","price","quantity"]

class Shopstockbookingform(forms.ModelForm):
    class Meta:
        model = Shopstockbooking
        fields = ["product","quantity","date","time","bookingstatus"]


class complaintform(forms.ModelForm):
    class Meta:
        model = complaint
        fields = ["reply"]
class helprequestform(forms.ModelForm):
    class Meta:
        model = helprequest
        fields = ["reply"]
class Supplycosubmitform(forms.ModelForm):
    class Meta:
        model = Supplycosubmit
        fields = ["stock","quantity"]
class Supplyconotifyform(forms.ModelForm):
    class Meta:
        model = Supplyconotification
        fields = ["userid","notification","date","time"]

class Userregistrationform(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields=['name','phoneno']

class shopform(forms.ModelForm):
    class Meta:
        model = Shop
        fields=['shopname','owner','location','address','phoneno','openingtime','closingtime']
        
class Supplycoform(forms.ModelForm):
    class Meta:
        model = Supplyco
        fields=['shopname','owner','location','address','phoneno','openingtime','closingtime']

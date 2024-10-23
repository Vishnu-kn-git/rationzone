from django import forms 
from .models import Submit,complaint,helprequest,Supplycosubmit,Supplyconotification
class Submitform(forms.ModelForm):
    class Meta:
        model = Submit
        fields = ["stock","quantity"]
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
        fields = ["userid","notification","date"]

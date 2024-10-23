from django.shortcuts import render,redirect
from django.views import View
from.models import Submit,feedback,complaint,helprequest,Supplycosubmit,Supplyconotification
from .forms import Submitform,complaintform,helprequestform,Supplycosubmitform,Supplyconotifyform

class Submitadd(View):
    def get(self,request):
        return render(request,"submit.html")
    def post(self,request):
        hij=Submitform(request.POST,request.FILES)
        if hij.is_valid():
            hij.save()
            return render(request,"submit.html")

class Table(View):
    def get(self,request):
        xyz=Submit.objects.all()
        return render(request,"table.html",{'x':xyz})
    
class Tabledit(View):
    #edit clicked
    def get(self,request,vijila):
        xyz=Submit.objects.filter(id=vijila).first()
        return render(request,'tableedit.html',{'x':xyz})
    #update form
    def post(self,request,vijila):
        xyz=Submit.objects.filter(id=vijila).first()
        hij=Submitform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            abc=Submit.objects.all()
            return render(request,"table.html",{'x':abc})
    
class Tabledelete(View):
    #edit clicked
    def get(self,request,vijila):
        xyz=Submit.objects.filter(id=vijila).first()
        return render(request,'tabledelete.html',{'x':xyz})
    #update form
    def post(self,request,vijila):
        xyz=Submit.objects.filter(id=vijila).first()
        xyz.delete()
        abc=Submit.objects.all()
        return render(request,"table.html",{'x':abc})
class feedbackclass(View):
    def get(self,request):
        xyz=feedback.objects.all()
        return render(request,"feedback.html",{'x':xyz})
class complaintclass(View):
    def get(self,request):
        xyz=complaint.objects.all()
        return render(request,"complaint.html",{'x':xyz})

class complaintedit(View):
    #edit clicked
    def get(self,request,comp):
        xyz=complaint.objects.filter(id=comp).first()
        return render(request,'complaintedit.html',{'x':xyz})
    #update form
    def post(self,request,comp):
        xyz=complaint.objects.filter(id=comp).first()
        hij=complaintform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            return redirect('complaintclass')
class helprequestclass(View):
    def get(self,request):
        xyz=helprequest.objects.all()
        return render(request,"helprequest.html",{'x':xyz})

class helprequestedit(View):
    #edit clicked
    def get(self,request,help):
        xyz=helprequest.objects.filter(id=help).first()
        return render(request,'helprequestedit.html',{'x':xyz})
    #update form
    def post(self,request,help):
        xyz=helprequest.objects.filter(id=help).first()
        hij=helprequestform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            return redirect('helprequestclass')

class Supplycosubmitadd(View):
    def get(self,request):
        return render(request,"supplycosubmit.html")
    def post(self,request):
        hij=Supplycosubmitform(request.POST,request.FILES)
        if hij.is_valid():
            hij.save()
            return render(request,"supplycosubmit.html")

class Supplycotable(View):
    def get(self,request):
        xyz=Supplycosubmit.objects.all()
        return render(request,"supplycotable.html",{'x':xyz})
    
class Supplycotabledit(View):
    #edit clicked
    def get(self,request,supedit):
        xyz=Supplycosubmit.objects.filter(id=supedit).first()
        return render(request,'supplycoedit.html',{'x':xyz})
    #update form
    def post(self,request,supedit):
        xyz=Supplycosubmit.objects.filter(id=supedit).first()
        hij=Supplycosubmitform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            abc=Supplycosubmit.objects.all()
            return render(request,"supplycotable.html",{'x':abc})
    
class Supplycotabledelete(View):
    #edit clicked
    def get(self,request,supedit):
        xyz=Supplycosubmit.objects.filter(id=supedit).first()
        return render(request,'supplycodelete.html',{'x':xyz})
    #update form
    def post(self,request,supedit):
        xyz=Supplycosubmit.objects.filter(id=supedit).first()
        xyz.delete()
        abc=Supplycosubmit.objects.all()
        return render(request,"supplycotable.html",{'x':abc})
    
class Supplyconotifyadd(View):
    def get(self,request):
        return render(request,"supplyconotifyapp.html")
    def post(self,request):
        hij=Supplyconotifyform(request.POST,request.FILES)
        if hij.is_valid():
            hij.save()
            return render(request,"supplyconotifyapp.html")

class Supplyconotify(View):
    def get(self,request):
        xyz=Supplyconotification.objects.all()
        return render(request,"supplyconotify.html",{'x':xyz})
    
class Supplyconotifyedit(View):
    #edit clicked
    def get(self,request,supnotedit):
        xyz=Supplyconotification.objects.filter(id=supnotedit).first()
        return render(request,'supplyconotifyedit.html',{'x':xyz})
    #update form
    def post(self,request,supnotedit):
        xyz=Supplyconotification.objects.filter(id=supnotedit).first()
        hij=Supplyconotifyform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            abc=Supplyconotification.objects.all()
            return render(request,"supplyconotify.html",{'x':abc})
    
class Supplyconotifydelete(View):
    #edit clicked
    def get(self,request,supnotedit):
        xyz=Supplyconotification.objects.filter(id=supnotedit).first()
        return render(request,'supplyconotifydelete.html',{'x':xyz})
    #update form
    def post(self,request,supnotedit):
        xyz=Supplyconotification.objects.filter(id=supnotedit).first()
        xyz.delete()
        abc=Supplyconotification.objects.all()
        return render(request,"supplyconotify.html",{'x':abc})

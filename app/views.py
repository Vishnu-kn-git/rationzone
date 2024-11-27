from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from .forms import *
from .models import *

class Admindashboard(View):
    def get(self,request):
        return render(request,"admindashboard.html")
class shopdashboard(View):
    def get(self,request):
        return render(request,"shopdashboard.html")
class supplycodashboard(View):
    def get(self,request):
        return render(request,"supplycodashboard.html")
    
class Feedbacktable(View):
    def get(self,request):
        xyz=feedback.objects.all()
        return render(request,"feedback.html",{'x':xyz})
    
class Shopusertable(View):
    def get(self,request):
        xyz=User.objects.all()
        return render(request,"shopusertable.html",{'x':xyz})
    

class Supplycousertable(View):
    def get(self,request):
        xyz=User.objects.all()
        return render(request,"supplycousertable.html",{'x':xyz})
    
class Adminusertable(View):
    def get(self,request):
        xyz=User.objects.all()
        return render(request,"adminusertable.html",{'x':xyz})


class Stockadd(View):
    def get(self,request):
        return render(request,"stockadd.html")
    def post(self,request):
        hij=Stockform(request.POST,request.FILES)
        if hij.is_valid():
            hij.save()
            return redirect("stocktable")
        


class Stocktable(View):
    def get(self,request):
        xyz=Stock.objects.all()
        return render(request,"stocktable.html",{'x':xyz})
    
class Stockedit(View):
    #edit clicked
    def get(self,request,stk):
        xyz=Stock.objects.filter(id=stk).first()
        return render(request,'stockedit.html',{'x':xyz})
    #update form
    def post(self,request,stk):
        xyz=Stock.objects.filter(id=stk).first()
        hij=Stockform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            abc=Stock.objects.all()
            return render(request,"stocktable.html",{'x':abc})
    
class Stockdelete(View):
    #edit clicked
    def get(self,request,stk):
        xyz=Stock.objects.filter(id=stk).first()
        return render(request,'stockdelete.html',{'x':xyz})
    #update form
    def post(self,request,stk):
        xyz=Stock.objects.filter(id=stk).first()
        xyz.delete()
        abc=Stock.objects.all()
        return render(request,"stocktable.html",{'x':abc})
    
class Supplycostockadd(View):
    def get(self,request):
        return render(request,"supplycostockadd.html")
    def post(self,request):
        hij=Supplycostockform(request.POST,request.FILES)
        if hij.is_valid():
            hij.save()
            return redirect("supplycostocktable")
        
class Supplycostocktable(View):
    def get(self,request):
        xyz=Supplycostock.objects.all()
        return render(request,"supplycostocktable.html",{'x':xyz})
    
class Supplycostockedit(View):
    #edit clicked
    def get(self,request,supstk):
        xyz=Supplycostock.objects.filter(id=supstk).first()
        return render(request,'supplycostockedit.html',{'x':xyz})
    #update form
    def post(self,request,supstk):
        xyz=Supplycostock.objects.filter(id=supstk).first()
        hij=Supplycostockform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            abc=Supplycostock.objects.all()
            return render(request,"supplycostocktable.html",{'x':abc})
        
class Supplycostockdelete(View):
    #edit clicked
    def get(self,request,supstk):
        xyz=Supplycostock.objects.filter(id=supstk).first()
        return render(request,'supplycostockdelete.html',{'x':xyz})
    #update form
    def post(self,request,supstk):
        xyz=Supplycostock.objects.filter(id=supstk).first()
        xyz.delete()
        abc=Supplycostock.objects.all()
        return render(request,"supplycostocktable.html",{'x':abc})

    

class Shopstockbookingadd(View):
    def get(self,request):
        return render(request,"shopstockbookingadd.html")
    def post(self,request):
        hij=Shopstockbookingform(request.POST,request.FILES)
        if hij.is_valid():
            hij.save()
            return redirect("shopstockbookingtable")
        
class Shopstockbookingtable(View):
    def get(self,request):
        xyz=Shopstockbooking.objects.all()
        return render(request,"shopstockbookingtable.html",{'x':xyz})
    
class Shopstockbookingedit(View):
    #edit clicked
    def get(self,request,shpbkng):
        xyz=Shopstockbooking.objects.filter(id=shpbkng).first()
        return render(request,'shopstockbookingedit.html',{'x':xyz})
    #update form
    def post(self,request,shpbkng):
        xyz=Shopstockbooking.objects.filter(id=shpbkng).first()
        hij=Shopstockbookingform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            abc=Shopstockbooking.objects.all()
            return render(request,"shopstockbookingtable.html",{'x':abc})
        
class Shopstockbookingdelete(View):
    #edit clicked
    def get(self,request,shpbkng):
        xyz=Shopstockbooking.objects.filter(id=shpbkng).first()
        return render(request,'shopstockbookingdelete.html',{'x':xyz})
    #update form
    def post(self,request,shpbkng):
        xyz=Shopstockbooking.objects.filter(id=shpbkng).first()
        xyz.delete()
        abc=Shopstockbooking.objects.all()
        return render(request,"shopstockbookingtable.html",{'x':abc})



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
            return redirect("supplyconotify")

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
    
class Userregistration(View):
    def get(self,request):
        return render(request,'registration.html')
    def post(self,request):
        f=Userregistrationform(request.POST)
        if f.is_valid():
            c=f.save(commit=False)
            c.login_id=Logintable.objects.create(username=request.POST['username'],password=request.POST['password'],type='user')
            c.save()
            return render(request,'registration.html')
        
class Userlogin(View):
    def get(self,request):
        return render(request,'userlogin.html')
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        try:
            v=Logintable.objects.get(username=username,password=password)
       

            if v.type=='shop' and v.status=='ACCEPT':
                return render(request,'shopdashboard.html')
            elif v.type=='supplyco' and v.status=='ACCEPT':
                return render(request,'supplycodashboard.html')
            elif v.type=='admin':
                return render(request,'admindashboard.html')
            
            else:
                return HttpResponse('''<script>alert(' not verified contact admin ');window.location.href='/app/userlogin/'</script>''')

        except Logintable.DoesNotExist:
            return HttpResponse('''<script>alert('Invalid credentials');window.location.href='/app/userlogin/'</script>''')
            
class shopadd(View):
    def get(self,request):
        return render(request,"shop.html")
    def post(self,request):
        hij=shopform(request.POST,request.FILES)

        if hij.is_valid():
            c=hij.save(commit=False)
            c.login_id=Logintable.objects.create(username=request.POST['username'],password=request.POST['password'],type='shop')
            c.save()
            return redirect("userlogin")
        
class shoptable(View):
    def get(self,request):
        xyz=Shop.objects.all()
        return render(request,"shoptable.html",{'x':xyz})

class shopaccept(View):
    #edit clicked
    def get(self,request,shp):
        xyz=Shop.objects.filter(id=shp).first()
        xyz.login_id.status='ACCEPT'
        xyz.login_id.save()
        return redirect('shoptable')
class shopreject(View):
    #edit clicked
    def get(self,request,shp):
        xyz=Shop.objects.filter(id=shp).first()
        xyz.login_id.status='REJECT'
        xyz.login_id.save()
        return redirect('shoptable')
class shopedit(View):
    #edit clicked
    def get(self,request,shp):
        xyz=Shop.objects.filter(id=shp).first()
        return render(request,'shopedit.html',{'x':xyz})
    #update form
    def post(self,request,shp):
        xyz=Shop.objects.filter(id=shp).first()
        hij=shopform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            abc=Shop.objects.all()
            return render(request,"shoptable.html",{'x':abc})
    
class Shopdelete(View):
    #edit clicked
    def get(self,request,shp):
        xyz=Shop.objects.filter(id=shp).first()
        return render(request,'shopdelete.html',{'x':xyz})
    #update form
    def post(self,request,shp):
        xyz=Shop.objects.filter(id=shp).first()
        xyz.delete()
        abc=Shop.objects.all()
        return render(request,"shoptable.html",{'x':abc})
    
class Supplycoadd(View):
    def get(self,request):
        return render(request,"supplycoregistration.html")
    def post(self,request):
        hij=Supplycoform(request.POST,request.FILES)

        if hij.is_valid():
            c=hij.save(commit=False)
            c.login_id=Logintable.objects.create(username=request.POST['username'],password=request.POST['password'],type='supplyco')
            c.save()
            return redirect("userlogin")
        
class Supplycotable(View):
    def get(self,request):
        xyz=Supplyco.objects.all()
        return render(request,"supplycotable.html",{'x':xyz})
    
class supplycoaccept(View):
    #edit clicked
    def get(self,request,shp):
        xyz=Supplyco.objects.filter(id=shp).first()
        xyz.login_id.status='ACCEPT'
        xyz.login_id.save()
        return redirect('supplycotable')
class supplycoreject(View):
    #edit clicked
    def get(self,request,shp):
        xyz=Supplyco.objects.filter(id=shp).first()
        xyz.login_id.status='REJECT'
        xyz.login_id.save()
        return redirect('supplycotable')

    
        
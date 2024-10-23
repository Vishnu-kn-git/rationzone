from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate
import json
from.models import Userprofile,Shop,Booking,Customerprofile
from .forms import Shopform,Bookingform,Bookingeditform

from loginapp.models import Userprofile,Token
class UserLogin(View):
    template_name ="login.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_type = ""
        response_dict = {"success": False}
        landing_page_url = {
                        "ADMIN": "user:loadadmin",
                        "INSTITUTE":"user:loadinstitute",
                        "TEACHER":"user:loadteacher",
                    }
        username = request.POST.get("username")
        password = request.POST.get("password")
        authenticated = authenticate(username=username, password=password)
        try:
            user = Userprofile.objects.get(username=username)
            print("hel")
        except Userprofile.DoesNotExist:
            response_dict[
                            "reason"
                        ] = "No account found for this username. Please signup."
            messages.error(request, response_dict["reason"])
        if not authenticated:
            response_dict["reason"] = "Invalid credentials."
            messages.error(request, response_dict["reason"])
            return redirect(request.GET.get("from") or "user:login")

        else:
            print("hello")
            session_dict = {"real_user": authenticated.id}
            token, c = Token.objects.get_or_create(
                        user=user, defaults={"session_dict": json.dumps(session_dict)}
                        )

            user_type = authenticated.user_type




            print("hai")
            print(user)
            print(user_type)

            return redirect(landing_page_url[user_type])
        return redirect(request.GET.get("from") or loadlogin)
    


class Shopadd(View):
    def get(self,request):
        return render(request,"shop.html")
    def post(self,request):
        hij=Shopform(request.POST,request.FILES)
        if hij.is_valid():
            hij.save()
            return render(request,"shop.html")
class Shoptable(View):
    def get(self,request):
        xyz=Shop.objects.all()
        return render(request,"shoptable.html",{'x':xyz})
    
class Shopedit(View):
    #edit clicked
    def get(self,request,sp):
        xyz=Shop.objects.filter(id=sp).first()
        return render(request,'shopedit.html',{'x':xyz})
    #update form
    def post(self,request,sp):
        xyz=Shop.objects.filter(id=sp).first()
        hij=Shopform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            abc=Shop.objects.all()
            return render(request,"shoptable.html",{'x':abc})
    
class Shopdelete(View):
    #edit clicked
    def get(self,request,sp):
        xyz=Shop.objects.filter(id=sp).first()
        return render(request,'shopdelete.html',{'x':xyz})
    #update form
    def post(self,request,sp):
        xyz=Shop.objects.filter(id=sp).first()
        xyz.delete()
        abc=Shop.objects.all()
        return render(request,"shoptable.html",{'x':abc})
    
class Bookingadd(View):
    def get(self,request):
        return render(request,"booking.html")
    def post(self,request):
        hij=Bookingform(request.POST,request.FILES)
        if hij.is_valid():
            hij.save()
            return redirect('bookingtable')
class Bookingtable(View):
    def get(self,request):
        xyz=Booking.objects.all()
        return render(request,"bookingtable.html",{'x':xyz})
    
class Bookingedit(View):
    #edit clicked
    def get(self,request,booking):
        xyz=Booking.objects.filter(id=booking).first()
        return render(request,'bookingedit.html',{'x':xyz})
    #update form
    def post(self,request,booking):
        xyz=Booking.objects.filter(id=booking).first()
        hij=Bookingeditform(request.POST,instance=xyz)
        if hij.is_valid():
            hij.save()
            abc=Booking.objects.all()
            return render(request,"bookingtable.html",{'x':abc})
    
class Bookingdelete(View):
    #edit clicked
    def get(self,request,booking):
        xyz=Booking.objects.filter(id=booking).first()
        return render(request,'bookingdelete.html',{'x':xyz})
    #update form
    def post(self,request,booking):
        xyz=Booking.objects.filter(id=booking).first()
        xyz.delete()
        abc=Booking.objects.all()
        return render(request,"bookingtable.html",{'x':abc})
    
class Customertable(View):
    def get(self,request):
        xyz=Customerprofile.objects.all()
        return render(request,"customertable.html",{'x':xyz})

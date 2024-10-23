from django.urls import path
from .views import Shopadd,Shoptable,Shopedit,Shopdelete,Bookingadd,Bookingtable,Bookingedit,Bookingdelete,Customertable
from loginapp.views import UserLogin

urlpatterns = [
    path("login/",UserLogin.as_view(),name="userlogin"),
    path('shopapp/',Shopadd.as_view()),
    path('shoptable/',Shoptable.as_view()),
    path('shopedit/<sp>',Shopedit.as_view()),
    path('shopdelete/<sp>',Shopdelete.as_view()),
    path('booking/',Bookingadd.as_view()),
    path('bookingtable/',Bookingtable.as_view(),name='bookingtable'),
    path('bookingedit/<booking>',Bookingedit.as_view()),
    path('bookingdelete/<booking>',Bookingdelete.as_view()),
    path('customertable/',Customertable.as_view())
    
]

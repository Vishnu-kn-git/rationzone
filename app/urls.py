from django.urls import path
from .views import *
urlpatterns = [
    path('stockadd/',Stockadd.as_view()),
    path('stocktable/',Stocktable.as_view(),name="stocktable"),
    path('stockedit/<stk>',Stockedit.as_view()),
    path('stockdelete/<stk>',Stockdelete.as_view()),

    path('supplycostockadd/',Supplycostockadd.as_view()),
    path('supplycostocktable/',Supplycostocktable.as_view(),name="supplycostocktable"),
    path('supplycostockedit/<supstk>',Supplycostockedit.as_view()),
    path('supplycostockdelete/<supstk>',Supplycostockdelete.as_view()),

    path('shopstockbookingadd/',Shopstockbookingadd.as_view()),
    path('shopstockbookingtable/',Shopstockbookingtable.as_view(),name="shopstockbookingtable"),
    path('shopstockbookingedit/<shpbkng>',Shopstockbookingedit.as_view()),
    path('shopstockbookingdelete/<shpbkng>',Shopstockbookingdelete.as_view()),

    path('shopusertable/',Shopusertable.as_view()),
    path('supplycousertable/',Supplycousertable.as_view()),
    path('adminusertable/',Adminusertable.as_view()),

    path('feedback/',Feedbacktable.as_view()),
    path('complaintclass/',complaintclass.as_view(),name='complaintclass'),
    path('complaintedit/<comp>',complaintedit.as_view()),
    path('helprequestclass/',helprequestclass.as_view(),name='helprequestclass'),
    path('helprequestedit/<help>',helprequestedit.as_view()),
    path('supplycosubmitapp/',Supplycosubmitadd.as_view()),
    path('supplycotable/',Supplycotable.as_view()),
    path('supplycotableedit/<supedit>',Supplycotabledit.as_view()),
    path('supplycotabledelete/<supedit>',Supplycotabledelete.as_view()),

    path('supplyconotifyapp/',Supplyconotifyadd.as_view()),
    path('supplyconotify/',Supplyconotify.as_view(),name="supplyconotify"),
    path('supplyconotifyedit/<supnotedit>',Supplyconotifyedit.as_view()),
    path('supplyconotifydelete/<supnotedit>',Supplyconotifydelete.as_view()),

    path("userregistration/",Userregistration.as_view()),
    path("userlogin/",Userlogin.as_view(),name="userlogin"),
    path("admindashboard/",Admindashboard.as_view(),name="admindashboard"),
    path("shopdashboard/",shopdashboard.as_view(),name="shopdashboard"),
    path("supplycodashboard/",supplycodashboard.as_view(),name="supplycodashboard"),
    path('shopadd/',shopadd.as_view()),
    path('shoptable/',shoptable.as_view(),name='shoptable'),
    path('shopaccept/<shp>',shopaccept.as_view()),
    path('shopreject/<shp>',shopreject.as_view()),
    path('shopedit/<shp>',Shopdelete.as_view()),
    path('supplycoadd/',Supplycoadd.as_view()),
    path('supplycotable/',Supplycotable.as_view(),name='supplycotable'),
    path('supplycoaccept/<shp>',supplycoaccept.as_view()),
    path('supplycoreject/<shp>',supplycoreject.as_view()),
]

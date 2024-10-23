from django.urls import path
from .views import Submitadd,Table,Tabledelete,Tabledit,feedbackclass,complaintclass,complaintedit,helprequestclass,helprequestedit
from .views import Supplycosubmitadd,Supplycotable,Supplycotabledit,Supplycotabledelete,Supplyconotifyadd,Supplyconotify,Supplyconotifyedit,Supplyconotifydelete
urlpatterns = [
    path('submitapp/',Submitadd.as_view()),
    path('table/',Table.as_view()),
    path('tableedit/<vijila>',Tabledit.as_view()),
    path('tabledelete/<vijila>',Tabledelete.as_view()),
    path('feedbackclass/',feedbackclass.as_view()),
    path('complaintclass/',complaintclass.as_view(),name='complaintclass'),
    path('complaintedit/<comp>',complaintedit.as_view()),
    path('helprequestclass/',helprequestclass.as_view(),name='helprequestclass'),
    path('helprequestedit/<help>',helprequestedit.as_view()),
    path('supplycosubmitapp/',Supplycosubmitadd.as_view()),
    path('supplycotable/',Supplycotable.as_view()),
    path('supplycotableedit/<supedit>',Supplycotabledit.as_view()),
    path('supplycotabledelete/<supedit>',Supplycotabledelete.as_view()),
    path('supplyconotifyapp/',Supplyconotifyadd.as_view()),
    path('supplyconotify/',Supplyconotify.as_view()),
    path('supplyconotifyedit/<supnotedit>',Supplyconotifyedit.as_view()),
    path('supplyconotifydelete/<supnotedit>',Supplyconotifydelete.as_view())
]

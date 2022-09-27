from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sts/',views.sts,name="sts"),
    path('bankers/',views.bankers,name="bankers"),
    path('PageRelocationAlgo/',views.pagereloc,name="pagereloc"),
    path('DiskSchedulingAlgo/',views.disksched,name="disksched"),

    path('sts-output/',views.stsoutput,name="stsoutput"),
    path('bankers-output/',views.bankersoutput,name="bankersoutput"),
    path('PageRelocationAlgo-output/',views.pagerelocoutput,name="pagerelocoutput"),
    # path('DiskSchedulingAlgo-output/',views.diskschedoutput,name="diskschedoutput"),
]
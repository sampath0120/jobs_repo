from django.shortcuts import render
from testapp.models import hydjobs
from testapp.models import punejobs
from testapp.models import bangulorjobs

# Create your views here.
def hydjob(request):
    hj=hydjobs.objects.all()
    return render(request,'testapp/HJ.html',{'hj':hj})
def banjob(request):
    bngj=bangulorjobs.objects.all()
    return render(request,'testapp/BJ.html',{'bngj':bngj})
def punejob(request):
    pj=punejobs.objects.all()
    return render(request,'testapp/PJ.html',{'pj':pj})
def homepage(request):
    return render(request,'index.html')

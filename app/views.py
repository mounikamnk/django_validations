from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def SF(request):
    SFO=studentform()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=studentform(request.POST)
        if SFD.is_valid():
            return HttpResponse('valid data')
        else:
            return HttpResponse('invalid')

    return render(request,'SF.HTML',d)
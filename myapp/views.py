from myapp.models import Admin_user
from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    context={}
    return render(request,'home.html',context)
def accounts(request):
    showit=False
    my_user=request.GET.get('login_type')
    phn=request.GET['phn']
    # print(phn)
    if my_user=='admin':
        exist=Admin_user.objects.filter(phone=phn).all()
        templist=Refrence_user.objects.all()
        if exist:
            return render(request,'AdminPage.html',{'list':templist})
        else:
            showit=True    
    else:
        exist=Refrence_user.objects.filter(phone=phn).all()
        if exist:
            return render(request,'refrence.html',{'list':exist})
        else:
            showit=True
    context={
        'showit':showit,
    }
    return render(request,'home.html',context)

def add(request):
    showit=False
    if request.method=="POST":
        st1=Refrence_user()
        st1.fullname=request.POST['fullname']
        st1.email=request.POST['email']
        st1.phone=request.POST['phn']
        st1.designation=request.POST['designation']
        st1.address=request.POST['address']
        number=Refrence_user.objects.filter(phone=st1.phone).all()
        if number:
            showit=True
        else:
            st1.save()
            templist=Refrence_user.objects.all()
            return render(request,'AdminPage.html',{'list':templist})
        
    return render(request,'add.html',{'showit':showit})
 
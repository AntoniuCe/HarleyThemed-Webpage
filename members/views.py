from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Member, Motorcycles,Orders,Facturare_pers_fizica
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import OrdersForm

def index(request):
    return render(request, 'home.html')

def magazin(request):
    motociclete = Motorcycles.objects.all()
    return render(request, 'magazin.html',{'motociclete':motociclete,})

def sportsters(request):
    sportsters = Motorcycles.objects.get(id=1)
    return render(request, 'sportsters.html',{'sportsters':sportsters,})

def softail(request):
    softail = Motorcycles.objects.get(id=2)
    return render(request, 'softail.html',{'softail':softail,})

def street(request):
    street = Motorcycles.objects.get(id=3)
    return render(request, 'street.html',{'street':street,})

def forty(request):
    forty = Motorcycles.objects.get(id=4)
    return render(request, 'forty_eight.html',{'forty':forty,})

def order(request):
    submitted = False
    order = OrdersForm(request.POST)
    if request.method == "POST":
        if order.is_valid():
            order.save()
            return HttpResponseRedirect('/?submitted=True')

    return render(request, 'order.html', { 'order': order})

def signup(request):
    if request.method == 'POST':
    
        username1=request.POST['username']

        email1=request.POST['email']
        
        password=request.POST['password']
        
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username1):
                messages.info(request, 'Username already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username1, email=email1, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords doesn t match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')
   

def login(request):
    if request.method == 'POST':
        username1=request.POST['username']
        password1=request.POST['password']
        user = auth.authenticate(username=username1, password = password1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials are incorrect')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
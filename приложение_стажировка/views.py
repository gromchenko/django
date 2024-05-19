from django.shortcuts import render, redirect
from .models import User, Question, FreeDateTime


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        service = request.POST['service']
        message = request.POST['message']
        q = Question()
        q.name = name
        q.email = email
        q.phone = phone
        q.view = service
        q.message = message
        q.save()
    return render(request,'index.html')

def about (request):
    return render(request, 'about.html')

def services (request):
    return render(request, 'services.html')

def contacts (request):
    return render(request, 'contacts.html')

def reg (request):
    if request.method == 'POST':
        fio = request.POST['fio']
        login = request.POST['login']
        password = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']
        user = User()
        user.fio = fio
        user.login = login
        user.password = password
        user.email = email
        user.phone = phone
        user.save()

    return render(request, 'reg.html')

def auth (request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        if User.objects.filter(login=login, password=password).exists():
            request.session['login'] = login

    return render(request, 'auth.html')

def price (request):
    return render(request, 'price.html')

def logoutuser (request):
    del request.session['login']
    return redirect('/')

def panel (request):
    freedatetimes = FreeDateTime.objects.filter(user=None)
    current_object_user = User.objects.filter(login=request.session['login']).first()
    datetimeusers = FreeDateTime.objects.filter(user=current_object_user)
    if request.method == 'POST':
        fio = request.POST['fio']
        email = request.POST['email']
        phone = request.POST['phone']
        User.objects.filter(login=request.session['login']).update(fio=fio, email=email, phone=phone)
    current_user = User.objects.filter(login=request.session['login']).first()
    return render(request, 'panel.html', context={'current_user':current_user, 'freedatetimes': freedatetimes, 'datetimeusers': datetimeusers})


def zap(request):
    if request.method == 'POST':
        id = request.POST['id']
        user = User.objects.filter(login=request.session['login']).first()
        FreeDateTime.objects.filter(id=id).update(user=user)

        return redirect('/panel')


from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login


def signupfunc(request):
    if request.method == 'POST':
        new_username = request.POST['username']
        new_password = request.POST['password']
        try:
            User.objects.get(username=new_username)
            return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(new_username, '', new_password)
            return render(request, 'signup.html', {'some': 100})
    return render(request, 'signup.html', {'some': 100})


def loginfunc(request):
    if request.method == 'POST':
        new_username = request.POST['username']
        new_password = request.POST['password']
        user = authenticate(request, username=new_username,
                            password=new_password)
        if user is not None:
            login(request, user)
            return redirect('signup')
        else:
            return redirect('login')
    return render(request, 'login.html')


def listfunc(request):
    return render(request, 'list.html')
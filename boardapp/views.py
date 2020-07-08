from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy


from boardapp.models import BoardModel


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
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')


@login_required()
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')


def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})


def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good += 1
    post.save()
    return redirect('list')


def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    login_username = request.user.get_username()
    if login_username in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext = post.readtext + ' ' + login_username
        post.save()
        return redirect('list')


class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')
from django.shortcuts import render



def signupfunc(requet):
    return render(requet, 'signup.html', {'some':100})
from django.urls import path

from boardapp.views import signupfunc
from boardapp.views import loginfunc
from boardapp.views import listfunc


urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
]

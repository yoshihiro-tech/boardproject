from django.urls import path


from boardapp.views import signupfunc
from boardapp.views import loginfunc
from boardapp.views import logoutfunc
from boardapp.views import listfunc
from boardapp.views import detailfunc
from boardapp.views import goodfunc


urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
]

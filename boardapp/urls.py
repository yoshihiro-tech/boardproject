from django.urls import path

from boardapp.views import signupfunc


urlpatterns = [
    path('signup/', signupfunc),
]

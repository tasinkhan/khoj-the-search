from django.conf.urls import url
from django.urls import path, include

from .views import index, registration_view, login_view, logout_view

app_name = "Usermodule"

urlpatterns = [
    path('', index, name='index'),
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
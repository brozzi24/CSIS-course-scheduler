
from django.urls import path

from . import views

urlpatterns = [
    path('',views.signIn, name='signin'),
    path('logout', views.logout, name='logout'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='schedule'),
    path('roomSearch',views.roomSearch, name='roomSearch'),
    path('timeSearch', views.timeSearch, name='timeSearch'),
    path('finalSchedule',views.finalSchedule, name='finalSchedule'),
    path('webSchedule',views.webSchedule, name='webSchedule'),
    path('defaultSemester', views.defaultSemester, name='defaultSemester')
    


]
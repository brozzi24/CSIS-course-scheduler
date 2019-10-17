from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from . import forms
from .models import Rooms
from scheduledClass.models import Scheduled
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        formRoom = forms.roomClass()
        rooms = Rooms.objects.all()
        if request.method == 'POST':
            for room in rooms:
                # Validate room is not already in database
                if room.room_number == int(request.POST['room_number']):
                    messages.error(request, 'There is already a room mathcing that room number')
                    return redirect('/rooms/')
            messages.success(request, 'Room has been added!')
            room_number = request.POST['room_number']
            room_type = request.POST['room_type']
            capcity = request.POST['capcity']

            room = Rooms(room_number=room_number,room_type=room_type,capcity=capcity)

            room.save()

            return redirect('/rooms/')

        

        time = [
            800,
            815,
            830,
            845,
            850,
            900,
            900,
            915,
            930,
            945,
            950,
            1000,
            1015,
            1030,
            1045,
            1050,
            1100,
            1115,
            1130,
            1145,
            1150,
            1200,
            1215,
            1230,
            1245,
            1250,
            1300
            
        ]

        time2 = []
        badTime = []

        ## for room search 
        test = Scheduled.objects.filter(room__room_number=352)

        for i in test:
            for j in time:
                if j >= i.start_time and j <= i.end_time:
                    if j in badTime:
                        continue
                    else:
                        badTime.append(j)

        for i in time:
            if i in badTime:
                continue
            else:
                time2.append(i)


        # for time search
        test2 = Scheduled.objects.filter(start_time__lte=900)
        test2 = Scheduled.objects.filter(end_time__gte=1000)

        tempRooms = []
        goodRooms = []
        
        for i in test2:
            if i.room in goodRooms:
                continue
            else:
                goodRooms.append(i.room)


        CONTEXT = {
            'rooms': rooms,
            'form': formRoom,
            'time': time2,
            'test': test,
            'bad': badTime,
            'good': goodRooms
        }

        formRoom = forms.roomClass()
        return render(request,'rooms/rooms.html',CONTEXT)
    else:
        messages.error(request,'You must be logged in to view this page')
        return redirect('signin')



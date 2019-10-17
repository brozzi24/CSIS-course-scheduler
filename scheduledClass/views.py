from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from rooms.models import Rooms

from .forms import roomForm
from .models import Scheduled
from rooms.models import Rooms
from classes.models import Classes

# Create your views here.
def index(request):
    form = roomForm()
    rooms = Rooms.objects.all()
    classes = Classes.objects.all()

    #Time
    time = [
        800,810,815,825,830,845,850,    
        900,910,915,925,930,945,950,
        1000,1010,1015,1025,1030,1045,1050,
        1100,1110,1115,1125,1130,1145,1150,
        1200,1210,1215,1225,1230,1245,1250,
        1300,1310,1315,1325,1330,1345,1350,
        1400,1410,1415,1425,1430,1445,1450,
        1500,1510,1515,1525,1530,1545,1550,
        1600,1610,1615,1625,1630,1645,1650,
        1700,1710,1715,1725,1730,1745,1750,
        1800,1810,1815,1825,1830,1845,1850,
        1900,1910,1915,1925,1930,1945,1950,
        2000,2010,2015,2025,2030,2045,2050,
        2100,2110,2115,2125,2130,2145,2150
    ]
    if request.method == 'POST' and request.POST['room'] == '0':
        #get course and room
        for course in classes:
            if course.name == request.POST['classes']:
                getCourse = course
        for room in rooms:
            if room.room_number == int(request.POST['room']):
                getRoom = room


        # get capacity, crn, and offering
        capacity = request.POST['capacity']
        crn = request.POST['crn']
        offering = request.POST['offering']

        # non-options WEB course info 
        building = 'WB'
        campus = 'OFF'
        delivery = 'WB'

        # optional WEB course info
        if request.POST['flex']:
            flex = request.POST['flex']
        else:
            flex = 1
        name = request.POST['name']
        banner_id = request.POST['banner_id']
        primary = request.POST['primary']
        notes = request.POST['notes']

        # create Scheduled object and save it
        scheduled = Scheduled(course = getCourse, room=getRoom, start_time=0, end_time=0,flex=flex,crn=crn,monday='',tuesday = '', wednesday = '', thursday = '', friday='',offering=offering,banner_id=banner_id,primary=primary,building=building,campus=campus,delivery=delivery,notes=notes,capacity=capacity)
        scheduled.save()
        return HttpResponseRedirect('/schedule/')

        # Schedule course
    elif request.method == 'POST':
        # Get course and Room
        getCourse = request.POST['classes']
        setCourse = Classes.objects.filter(name__iexact=getCourse)
        # Turn room id to int
        getRoom = request.POST['room']
        room_id = int(getRoom)
        setRoom = Rooms.objects.filter(room_number=room_id)
        # Days of week
        monday = ''
        tuesday = ''
        wednesday = ''
        thursday = ''
        friday = ''
        
        
        # For scheduled database
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        if request.POST['flex']:
            flex = request.POST['flex']
        else:
            flex = 1
        crn = request.POST['crn']
        offering = request.POST['offering']
        name = request.POST['name']
        banner_id = request.POST['banner_id']
        primary = request.POST['primary']
        if request.POST['building']:
            building = request.POST['building']
        else:
            building = '8'
        if request.POST['campus']:
            campus = request.POST['campus']
        else:
            campus = "M"
        if request.POST['delivery']:
            delivery = request.POST['delivery']
        else:
            delivery = "TR"
        days = request.POST.getlist('days[]')
        # Get the days checkboxes
        for day in days:
            if day == 'M':
                monday = day
            if day == 'T':
                tuesday = day
            if day == 'W':
                wednesday = day
            if day == 'H':
                thursday = day
            if day == 'F':
                friday = day   
        notes = request.POST['notes']
        
        # Scheduled object
        scheduled = Scheduled(course = setCourse[0], room=setRoom[0], start_time=start_time, end_time=end_time,flex=flex,crn=crn,monday=monday,tuesday = tuesday, wednesday = wednesday, thursday = thursday, friday=friday,offering=offering,banner_id=banner_id,primary=primary,building=building,campus=campus,delivery=delivery,notes=notes,capacity=0)
        scheduled.save()

        return HttpResponseRedirect('/schedule/')
        
    context = {
        'form': form,
        'rooms': rooms,
        'time': time,
        'classes': classes
    }
    return render(request,'schedule/schedule.html',context)


def roomSearch(request):
    # Database objects needed
    rooms = Rooms.objects.all()
    classes = Classes.objects.all()
    # Form data need
    room_id = request.GET.get('room')
    days = request.GET.getlist('days[]')
    roomID = int(room_id)
    
    # Times
    time = [
        800,810,815,825,830,845,850,    
        900,910,915,925,930,945,950,
        1000,1010,1015,1025,1030,1045,1050,
        1100,1110,1115,1125,1130,1145,1150,
        1200,1210,1215,1225,1230,1245,1250,
        1300,1310,1315,1325,1330,1345,1350,
        1400,1410,1415,1425,1430,1445,1450,
        1500,1510,1515,1525,1530,1545,1550,
        1600,1610,1615,1625,1630,1645,1650,
        1700,1710,1715,1725,1730,1745,1750,
        1800,1810,1815,1825,1830,1845,1850,
        1900,1910,1915,1925,1930,1945,1950,
        2000,2010,2015,2025,2030,2045,2050,
        2100,2110,2115,2125,2130,2145,2150
    ]

    # Get good and bad times
    goodTime = []
    badTime = []
    selectedRoom = Scheduled.objects.filter(room__room_number=room_id)
    selectedDays = []
    # Get selected days that are scheduled
    for day in days:
        if day == 'M':
            selectedDays += selectedRoom.filter(monday__iexact='M')
        if day == 'T':
            selectedDays += selectedRoom.filter(tuesday__iexact='T')
        if day == 'W':
            selectedDays += selectedRoom.filter(wednesday__iexact='W')
        if day == 'H':
            selectedDays += selectedRoom.filter(thursday__iexact='H')
        if day == 'F':
            selectedDays += selectedRoom.filter(friday__iexact='F')
    

    # Check if a givin time is available for a class        
    for i in selectedDays:
        for j in time:
            if j >= i.start_time and j <= i.end_time:
                if j in badTime:
                    continue
                else:
                    badTime.append(j)
    # Add good time to a list
    for i in time:
        if i in badTime:
            continue
        else:
            goodTime.append(i)

    context = {
        'rooms': rooms,
        'classes': classes,
        'values': request.GET,
        'roomID': roomID,
        'time': goodTime,
        'days': days
    }
    return render(request, 'schedule/roomSchedule.html',context)

def finalSchedule(request):
    schedule = Scheduled.objects.all()
    rooms = Rooms.objects.all()

    context = {
        'schedule': schedule
       
    }
    return render(request, 'schedule/finalSchedules.html',context)

def timeSearch(request):
    # Database objects needed
    rooms = Rooms.objects.all()
    classes = Classes.objects.all()
    scheduled = Scheduled.objects.all()
    # GET vars needed
    days = request.GET.getlist('days[]')
    start_time = int(request.GET.get('start_time'))
    end_time = int(request.GET.get('end_time'))
    room_type = request.GET.get('room_type')


    # get days of the week selected by user
    selectedDays = []
    # Get scheduled class on selected days
    for day in days:
        if day == 'M':
            selectedDays += scheduled.filter(monday__iexact='M')
        if day == 'T':
            selectedDays += scheduled.filter(tuesday__iexact='T')
        if day == 'W':
            selectedDays += scheduled.filter(wednesday__iexact='W')
        if day == 'H':
            selectedDays += scheduled.filter(thursday__iexact='H')
        if day == 'F':
            selectedDays += scheduled.filter(friday__iexact='F')

    # Check to see if each classroom is open at a selected time 
    badRooms = set()
    goodRooms = []
    for i in selectedDays:
        print(i.room)
        if i.end_time >= start_time and i.end_time <= end_time:
            badRooms.add(i.room)
        elif i.start_time >= start_time and i.end_time <= end_time:
            badRooms.add(i.room)
        elif i.start_time >= start_time and i.start_time <= end_time:
            badRooms.add(i.room)
        elif i.start_time <= start_time and i.end_time >= end_time:
            badRooms.add(i.room)
        
    # add open rooms to goodRooms list
    for room in rooms:
        if room not in badRooms and room.room_type == room_type.upper():
            goodRooms.append(room)


    context = {
        'rooms': rooms,
        'classes': classes,
        'days': days,
        'start': start_time,
        'end': end_time,
        'goodRooms': goodRooms 
    }
    return render(request,'schedule/timeSchedule.html',context)


def webSchedule(request):
    # Get user form information
    classes = Classes.objects.all()
    
    web = 'WEB'

    context = {
        'classes': classes,
        'values': request.GET
    }
    return render(request,'schedule/webSchedule.html',context)
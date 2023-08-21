from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate, login

from home.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.messages import constants as messages
from django.contrib import messages

def home(request):
    return render(request, 'home.html')
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/index")

        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid Username or Password')
            return render(request, 'login.html')
            
 
        

    return render(request, 'login.html')

def regUser(request):
    if request.method=='POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']

        # check if user has entered correct credentials
        data = User.objects.create_user(first_name=first_name,last_name=last_name,username=username, password=password)
        data.save()
        messages.success(request, 'Registered successfully!')
        return render(request, 'reg.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
def about(request):
    return render(request, 'about.html')
def reg(request):
    return render(request, 'reg.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
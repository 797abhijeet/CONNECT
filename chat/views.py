# chat/views.py
from django.shortcuts import render, redirect
from chat.models import Group, Message
from django.http import HttpResponse, JsonResponse

def home(request):
    # Your home view logic here
    return render(request, 'home.html')

def group(request, group):
    # Your group view logic here
    return render(request, 'group.html', {'group': group})

def checkview(request):
    # Your checkview logic here
    return HttpResponse("Checkview")

def send(request):
    # Your send logic here
    return HttpResponse("Send")

def getMessages(request, group):
    # Your getMessages logic here
    return JsonResponse({"messages": []})

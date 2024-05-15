from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello world. You are at rapsingh Django home Page")
    return render(request,'index.html')

def about(request):
    return HttpResponse("Hello world. You are at rapsingh Django about Page")


def contact(request):
    return HttpResponse("Hello world. You are at rapsingh Django contact Page")

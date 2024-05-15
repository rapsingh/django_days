from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world. You are at rapsingh Django home Page")


def about(request):
    return HttpResponse("Hello world. You are at rapsingh Django about Page")


def contact(request):
    return HttpResponse("Hello world. You are at rapsingh Django contact Page")

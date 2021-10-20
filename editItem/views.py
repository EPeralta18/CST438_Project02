from django.shortcuts import render

def index(request):
    return render(request, "editItem/edit.html")
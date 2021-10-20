from django.shortcuts import render

def index(request):
    return render(request, "edit/edit.html")
from django.shortcuts import render

def index(request):
    return render(request, "editAccount/editAccount.html")

from django.shortcuts import render, redirect
from Firebase import Firebase

def index(request):
    if request.method == 'POST':
        firebase = Firebase()
        username = request.POST['username']
        password = request.POST['password']
        request.session['username'] = username
        user = firebase.authUser(username, password)
        if user != None:
            return redirect('../items')
        else: 
            return render(request, 'login.html', {'loginFailed': True})
    else:
        return render(request, "login.html")

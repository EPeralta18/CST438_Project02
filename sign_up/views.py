from django.shortcuts import render, redirect
from Firebase import Firebase

# Create your views here.


def index(request):
    if request.method == 'POST':
        firebase = Firebase()
        username = request.POST['username'].lstrip()
        password = request.POST['password']
        if ' ' in username:
            data = {'message':'Enter valid username', 'class':'text-danger'}
            return render(request, 'sign_up.html', data)
        if ' ' in password:
            data = {'message':'Enter valid password', 'class':'text-danger'}
            return render(request, 'sign_up.html', data)
        request.session['username'] == ""
        user = firebase.getUser(username)
        if user == None:
            firebase.addUser(username, password)
            data = {'message':'Account created successfully', 'class':'text-success'}
            return render(request, 'sign_up.html', data)
        else:
            data = {'message':'Username already in use', 'class':'text-danger'}
        return render(request, 'sign_up.html', data)
    else:
        return render(request, 'sign_up.html')

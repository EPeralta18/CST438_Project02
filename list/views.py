from django.shortcuts import render, redirect
from Firebase import Firebase

def index(request):
    firebase = Firebase()
    username = request.session['username']
    items = firebase.getItem(firebase.getUserWishlist(username))
    data = {
        'username': username,
        'items': items
    }
    return render(request, 'list.html', data)
    
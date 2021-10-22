from django.shortcuts import render, redirect
from Firebase import Firebase

def index(request):
    firebase = Firebase()
    username = request.session['username']
    items = firebase.getItem(firebase.getUserWishlist(username))
    print(items)
    data = {
        'username': username,
        'items': items
    }
    return render(request, 'list.html', data)
    
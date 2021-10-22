from django.shortcuts import render, redirect
from Firebase import Firebase

def index(request):
    firebase = Firebase()
    username = request.session['username']
    wishlist = firebase.getUserWishlist(username)
    if wishlist == None:
        return render(request, 'list.html', {'username':username, 'items':'No items found in wishlist'})
    items = firebase.getItem(wishlist)

    data = {
        'username': username,
        'items': items
    }
    return render(request, 'list.html', data)
    
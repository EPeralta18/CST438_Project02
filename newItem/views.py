from django.shortcuts import render, redirect
from Firebase import Firebase

def index(request):
    if request.method == 'POST':
        firebase = Firebase()
        itemName = request.POST['itemName']
        description = request.POST['Description']
        image = request.POST['image']
        url = request.POST['URL']
        username = request.session['username']
        user = firebase.getUser(username)


        if description == "":
            descriptions = "no description";
        if itemName == "":
            itemName == "no item given";
        if url == "":
            url = "no URL";
        if image == "":
            image = "no Image";


        if user != None:
            firebase.addItem(itemName, url, image, description)
        else:
            return render(request, 'newItem.html', {'loginFailed': True})
    else:
        return render(request, "newItem.html")

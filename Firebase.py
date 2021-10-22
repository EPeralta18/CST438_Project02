from pyasn1.type.univ import Null
import pyrebase
class Firebase:
    def __init__(self):
        self.config = {
            "apiKey": "AIzaSyDjDMxS20gu5lD9rRdnx2hGvcbaQulrqeA",
            "authDomain": "cst438-project2-8bdae.firebaseapp.com",
            "databaseURL": "https://cst438-project2-8bdae-default-rtdb.firebaseio.com",
            "projectId": "cst438-project2-8bdae",
            "storageBucket": "cst438-project2-8bdae.appspot.com",
            "messagingSenderId": "658228043024",
            "appId": "1:658228043024:web:63606d2de17b5690b61995"
        }
        self.firebase = pyrebase.initialize_app(self.config)
        self.auth = self.firebase.auth()
        self.database = self.firebase.database()
    def getItems(self):
        return self.database.child('items').get().val()
    def getUsers(self):
        return self.database.child('users').get().val()
    def authUser(self, username, password):
        users = self.getUsers()
        for key in users:
            if users[key]['username'] == username and users[key]['password'] == password:
                return users[key]
        return None
    def getUser(self, username):
        users = self.getUsers()
        for key in users:
            if users[key]['username'] == username:
                return users[key], key
        return None
    def getUserWishlist(self, username):
        try:
            return self.database.child('wishlist').get().val()[username]
        except:
            return None
    def getItem(self, index):
        items = self.getItems()
        return [items[index[key]] for key in index]
    def addUser(self, username, password):
        data = {
            "adminStatus": False,
            "password": password,
            "username": username
        }
        self.database.child('users').push(data)
    def removeUser(self, username):
        user, key = self.getUser(username)
        self.database.child('users').child(key).remove()
    def setAdminStatus(self, username, adminStatus):
        user, key = self.getUser(username)
        self.database.child('users').child(
            key).update({"adminStatus": adminStatus})
    def addItem(self, name, itemLink, image='No Image', description='No description'):
        items = self.getItems()
        data = {
            "name": name,
            "link": itemLink,
            "image": image,
            "description": description,
        }
        self.database.child('items').push(data)
        return self.getItemKey(name, itemLink, image, description)
    def addItemToUserWishlist(self, username, itemKey):
        self.database.child('wishlist').child(username).push(itemKey)
    def getItemKey(self, name, link, image='No Image', description='No description'):
        items = self.getItems()
        for key in items:
            if items[key]["name"] == name and items[key]["link"] == link and items[key]["image"] == image and items[key]["description"] == description:
                return key
        return None
    def removeItem(self, key):
        self.database.child('items').child(key).remove()
    def removeItemFromWishlist(self, username, itemKey):
        wishlist = self.getUserWishlist(username)
        for i in wishlist:
            if wishlist[i] == itemKey:
                self.database.child('wishlist').child(
                    username).child(i).remove()

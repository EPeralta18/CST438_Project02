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

    def getUser(self, username):
      for user in self.getUsers():
        if user["username"] == username:
          return user
      return Null

    def getUserWishlist(self, username):
      return self.database.child('wishlist').get().val()[username]
    
    def getItem(self, index):
      items = self.getItems()
      return [items[i] for i in index]




firebase = Firebase()

print(firebase.getItems())

print(firebase.getUsers())

print(firebase.getUser("user2"))

print(firebase.getUserWishlist("user1"))

print(firebase.getItem(firebase.getUserWishlist("user1")))
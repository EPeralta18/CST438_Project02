 // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.1.2/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.1.2/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyDjDMxS20gu5lD9rRdnx2hGvcbaQulrqeA",
    authDomain: "cst438-project2-8bdae.firebaseapp.com",
    databaseURL: "https://cst438-project2-8bdae-default-rtdb.firebaseio.com",
    projectId: "cst438-project2-8bdae",
    storageBucket: "cst438-project2-8bdae.appspot.com",
    messagingSenderId: "658228043024",
    appId: "1:658228043024:web:63606d2de17b5690b61995",
    measurementId: "G-ZDFLGNQCXG"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
  //signup function
  function signUp()
  {
    var user = document.getElementById("User");
    var password = document.getElementById("Pass");
    const promise = auth.createUserWithUserAndPassword(user.value,password.value);
    promise.catch(e=>alert(e.message));
    alert("SignUp Successfully");
  }

  //signIN function
  function  signIn()
  {
    var user = document.getElementById("User");
    var password = document.getElementById("Pass");
    const promise = auth.signInWithEmailAndPassword(user.value,password.value);
    promise.catch(e=>alert(e.message));
  }


  //signOut

  function signOut(){
    auth.signOut();
    alert("SignOut Successfully from System");
  }

  //active user to homepage
  firebase.auth().onAuthStateChanged((user)=>{
    if(user){
      var User = user.User;
      alert("Active user "+User);
    }
    else
    {
      alert("No Active user Found")
    }
  })
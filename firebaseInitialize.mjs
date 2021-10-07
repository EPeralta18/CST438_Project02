import { initializeApp } from 'firebase/app';
// import { getFirestore, collection, getDocs } from 'firebase/firestore/lite';
import { getDatabase, ref, set, onValue, child, get } from "firebase/database";

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

const app = initializeApp(firebaseConfig);
const db = getDatabase();
const dbRef = ref(db);

const getUsers = async (dbRef) => {
  get(child(dbRef, `users`)).then((snapshot) => {
    if (snapshot.exists()) {
      console.log(snapshot.val());
    } else {
      console.log("No data available");
    }
  }).catch((error) => {
    console.log(error);
  })
}

getUsers(dbRef);
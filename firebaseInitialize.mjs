import { initializeApp } from 'firebase/app';
import {getFirestore, collection, getDocs} from 'firebase/firestore/lite';

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
const db = getFirestore(app);

const getUsers = async(db) => {
  console.log(db);
}

getUsers(db);
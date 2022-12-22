import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAVBr_YE-XjHIe7EWaUnU5h8tPPetpYUo8",
  authDomain: "smart-city-54346.firebaseapp.com",
  projectId: "smart-city-54346",
  storageBucket: "smart-city-54346.appspot.com",
  messagingSenderId: "362437088055",
  appId: "1:362437088055:web:698f9200c0e652caa740b2",
  measurementId: "G-ZJ9HC1C3KS"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

export {app, db};
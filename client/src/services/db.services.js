import { db } from '../firebase/app';
import { doc, getDocs, getDoc, collection, setDoc, query, Timestamp, where, deleteDoc } from "firebase/firestore";

export const dbService = {
  fetchSpaces,
}

async function fetchSpaces() {
  let spaces = [];
  const spacesCollection = collection(db, 'spaces');
  const querySpaces = await getDocs(spacesCollection);
  const totalSpaces = querySpaces.size
  querySpaces.docs.map(docSpace => {
    spaces.push(JSON.parse(JSON.stringify(docSpace.data())))
  });
  const freeSpaces = spaces.filter(
    (space) => space.occupied === false
  );
  return `${freeSpaces.length}/${totalSpaces}`
};
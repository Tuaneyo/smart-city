import { db } from '../firebase/app';
import { getDocs, query, limit, collection, doc, getDoc} from "firebase/firestore";
import { CalculationServie } from './calculation';

export const dbService = {
  getParkingStats,
  fetchCarParking,
  fetchParked
}

async function getParkingStats() {
  const parked = await fetchCollection('parked');
  const freeSpaces = await fetchSpaces();

  const total = []
  const spaces = [];
  // eslint-disable-next-line array-callback-return
  parked.data.map((parking) => {
    total.push(parking.total)
    spaces.push(parking.space_id)
  });

  const mean = CalculationServie.mean(total).toString()
  const mode = CalculationServie.mode(spaces).toString()
  const median = CalculationServie.median(spaces).toString()

  return {freeSpaces: freeSpaces, mean: mean, mode: mode, median: median}
}

async function fetchSpaces() {
  const spaces = await fetchCollection('spaces')
  const totalSpaces = spaces.size
  const freeSpaces = spaces.data.filter(
    (space) => space.occupied === false
  );
  return `${freeSpaces.length}/${totalSpaces}`
};

const fetchCollection = async (name, maxLimit = 100) => {
  let data = [];
  const dataCollection = query(collection(db, name), limit(maxLimit))
  const queryData = await getDocs(dataCollection);
  // eslint-disable-next-line array-callback-return
  queryData.docs.map(doc => {
    data.push(JSON.parse(JSON.stringify(doc.data())))
  });
  return {size: queryData.size, data: data};
}

async function fetchCarParking() {
  const parkingCars = await getDoc(doc(db, "parking", "cars"))
  const parkingData = JSON.parse(JSON.stringify(parkingCars.data()))

  const orderedParkingData = Object.keys(parkingData).sort().reduce(
    (obj, key) => { 
      obj[key] = parkingData[key]; 
      return obj;
    }, 
    {}
  );

  const pastDaysParking = Object.keys(orderedParkingData).reverse().slice(0, 7).reduce((result, key) => {
      result[key] = orderedParkingData[key];

      return result;
  }, {});
  return pastDaysParking
}

async function fetchParked() {
  const parked = await fetchCollection('parked', 10)
  // console.log('parked', parked);
  return parked
}
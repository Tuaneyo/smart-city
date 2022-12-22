import React, { useEffect, useState } from "react";
import { dbService } from "../../services/db.services";
import moment from 'moment';

// components

export default function CardPageVisits() {
  const [parkedData, setParkedData] = useState({})

  useEffect(() => {
    const getParkedData = async () => {
      const parkedStats = await dbService.fetchParked()
      setParkedData(parkedStats)
    }
    getParkedData()
  }, [])

  const test = () => {

    
    parkedData.data?.map((parked) => {
      const formatted = moment.utc(parked.start.seconds*1000).format('DD-MM-yyyy HH:mm');
      console.log(formatted);
      // Object.keys(dataObj).map((key, idx) => {
      //   console.log(idx);
      // })
    })
  }

  return (
    <>
      <div className="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded">
        <div className="rounded-t mb-0 px-4 py-3 border-0">
          <div className="flex flex-wrap items-center">
            <div className="relative w-full px-4 max-w-full flex-grow flex-1">
              <h3 className="font-semibold text-base text-blueGray-700" onClick={test}>
                Geparkeerd lijst 
              </h3>
            </div>
            
          </div>
        </div>
        <div className="block w-full overflow-x-auto">
          {/* Projects table */}
          <table className="items-center w-full bg-transparent border-collapse">
            <thead>
              <tr>
                <th className="px-6 bg-blueGray-50 text-blueGray-500 align-middle border border-solid border-blueGray-100 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                  Parkeervak nummer {parkedData.size}
                </th>
                <th className="px-6 bg-blueGray-50 text-blueGray-500 align-middle border border-solid border-blueGray-100 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                  Parkeertijd (s)
                </th>
                <th className="px-6 bg-blueGray-50 text-blueGray-500 align-middle border border-solid border-blueGray-100 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                  Datum
                </th>
                <th className="px-6 bg-blueGray-50 text-blueGray-500 align-middle border border-solid border-blueGray-100 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                  startijd
                </th>
                <th className="px-6 bg-blueGray-50 text-blueGray-500 align-middle border border-solid border-blueGray-100 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                  eindtijd
                </th>
              </tr>
            </thead>
            <tbody>
              { parkedData.data?.map((parked, idx) => {
                  return (
                    <tr key={idx}>
                     <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left">
                        { parked.space_id }
                      </th>
                      <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left">
                        { parked.total }
                      </th>
                      <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left">
                        { moment.utc(parked.start.seconds*1000).format('DD-MM-yyyy') }
                      </th>
                      <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left">
                        { moment.utc(parked.start.seconds*1000).format('HH:mm:ss') }
                      </th>
                      <th className="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left">
                        { moment.utc(parked.end.seconds*1000).format('HH:mm:ss') }
                      </th>
                    </tr>
                  )
                })}
               
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}

import React, { useEffect, useState } from "react";

// components

import CardStats from "../Cards/CardStats.js";
import { dbService } from "../../services/db.services.js";

export default function HeaderStats() {
  const [data, setData] = useState([
    {
      title: 'Parkeer plaatsen vrij',
      statDescription: 'vrije parkeerplekken en het totaal',
      statValue: '0',
      color: 'bg-green-500'
    },
    {
      title: 'Gemiddeld parkeertijd',
      statDescription: 'Eenheid in secondes',
      statValue: '',
      color: 'bg-orange-500'
    },
    {
      title: 'Favorite parkeervak',
      statDescription: 'Meest gebruikte parkeervak',
      statValue: '',
      color: 'bg-pink-500'
    },
    {
      title: 'Mediaan waarde ',
      statDescription: 'Van de parkeertijd datasets',
      statValue: 'Dicht',
      color: 'bg-purple-500'
    },
  ])

  useEffect(() => {
    
    const getStats = async () => {
      const parkingStats = await dbService.getParkingStats()
      // eslint-disable-next-line array-callback-return
      Object.keys(parkingStats).map((valueKey, idx) => {
        updateStatsState(parkingStats[valueKey], idx)
      })

      await dbService.fetchCarParking()
    }
    getStats();

  }, [])

  const updateStatsState = (data, index) => {
    setData(current =>
      current.map((obj, idx) => {
        if (idx === index) {
          return {...obj, statValue: data};
        }
        return obj;
      }),
    );
  }

  return (
    <>
      {/* Header */}
      <div className="relative bg-sky-600 md:pt-32 pb-32 pt-12">
        <div className="px-4 md:px-10 mx-auto w-full">
          <div>
            {/* Card stats */}
            <div className="flex flex-wrap">
              {data.map((item, idx) => {
                return (
                  <React.Fragment key={idx}>
                    <div className="w-full lg:w-6/12 xl:w-3/12 px-4">
                      <CardStats
                        statSubtitle={item.title}
                        statTitle={item.statValue}
                        statArrow="up"
                        statIconName="far fa-chart-bar"
                        statIconColor={item.color}
                        statDescripiron={item.statDescription}
                      />
                    </div>
                  </React.Fragment>
                )
              })}
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

import React, { useEffect, useState } from "react";

// components

import CardStats from "../Cards/CardStats.js";
import { dbService } from "../../services/db.services.js";

export default function HeaderStats() {
  const [data, setData] = useState([
    {
      title: 'Plaatsen vrij',
      statValue: '1',
      color: 'bg-green-500'
    },
    {
      title: 'Gemiddeld parkeertijd',
      statValue: '',
      color: 'bg-orange-500'
    },
    {
      title: 'Meest gebruikt parkeervak',
      statValue: '',
      color: 'bg-pink-500'
    },
    {
      title: 'Slagboom ',
      statValue: 'Dicht',
      color: 'bg-purple-500'
    },
  ])

  useEffect(() => {
    
    const freeSpaces = async () => {
      const freeSpaces = await dbService.fetchSpaces();
      console.log(freeSpaces);
      setData(current =>
        current.map((obj, idx) => {
          if (idx === 0) {
            return {...obj, statValue: freeSpaces};
          }
          return obj;
        }),
      );
    }
    freeSpaces();

    
  }, [])

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

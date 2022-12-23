import React from "react";

// components

import CardBarChart from "../components/Cards/CardBarChart.js";
import CardBarTable from "../components/Cards/CardBarTable.js";

export default function Dashboard() {
  return (
    <>
      <div className="flex flex-wrap">
        <div className="w-full xl:w-8/12 mb-12 xl:mb-0 px-4">
          <CardBarChart />
        </div>
      </div>
      <div className="flex flex-wrap mt-4">
        <div className="w-full xl:w-full mb-12 xl:mb-0 px-4">
          <CardBarTable />
        </div>
      </div>
    </>
  );
}

import './App.css';
import React from 'react';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

import DashboardLayout from "./layouts/Dashboard.js";

const router = createBrowserRouter([
  {
    path: "/",
    element: <DashboardLayout />,
  },
]);

const App = () => {
  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;

import { useState } from "react";
import { Routes, Route } from "react-router-dom";
import Topbar from "./scenes/global/Topbar";
import Sidebar from "./scenes/global/Sidebar";
// import Dashboard from "./scenes/dashboard";
import Hotel from "./scenes/services/hotel";
import Flight from "./scenes/services/flight";
import Tour from "./scenes/services/tour";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { ColorModeContext, useMode } from "./theme";
import HOTEL from "./scenes/bookings/hotel";
import FLIGHT from "./scenes/bookings/flight";
import TOUR from "./scenes/bookings/tour";
import User from "./scenes/user";

function App() {
  const [theme, colorMode] = useMode();
  const [isSidebar, setIsSidebar] = useState(true);

  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="app">
          <Sidebar isSidebar={isSidebar} />
          <main className="content">
            <Topbar setIsSidebar={setIsSidebar} />
            <Routes>
              {/* <Route path="/dashboard" element={<Dashboard />} /> */}
              <Route path="/service/hotel" element={<Hotel />} />
              <Route path="/service/flight" element={<Flight />} />
              <Route path="/service/tour" element={<Tour />} />
              <Route path="/booking/hotel" element={<HOTEL />} />
              <Route path="/booking/flight" element={<FLIGHT />} />
              <Route path="/booking/tour" element={<TOUR />} />
              <Route path="/users" element={<User />} />
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;

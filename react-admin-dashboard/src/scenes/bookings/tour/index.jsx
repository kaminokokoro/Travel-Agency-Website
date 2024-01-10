import {
    Box,
    Typography,
    useTheme,
  } from "@mui/material";
  import { DataGrid } from "@mui/x-data-grid";
  import { tokens } from "../../../theme";
  import { mockDataBookingTours } from "../../../data/mockData";
  import Header from "../../../components/Header";
  
  const TOUR = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    const columns = [
      { 
        field: "id",
        headerName: "ID" 
      },
      {
        field: "tourName",
        headerName: "Tour",
        flex: 1,
        cellClassName: "name-column--cell"
      },
      {
        field: "departureDate",
        headerName: "Departure",
        flex: 1,
      },
      {
        field: "returnDate",
        headerName: "Return",
        flex: 1,
      },
      {
        field: "userBooked",
        headerName: "User Booked",
        flex: 1,
        cellClassName: "name-column--cell"
      },
      {
        field: "paymentTime",
        headerName: "Payment Time",
        flex: 1,
      },
    ];
  
    return (
      <Box m="20px">
        <Header title="FLIGHTS BOOKING" subtitle="List of Flights" />
        <Box
          m="40px 0 0 0"
          height="75vh"
          sx={{
            "& .MuiDataGrid-root": {
              border: "none",
            },
            "& .MuiDataGrid-cell": {
              borderBottom: "none",
            },
            "& .name-column--cell": {
              color: colors.greenAccent[300],
            },
            "& .MuiDataGrid-columnHeaders": {
              backgroundColor: colors.blueAccent[700],
              borderBottom: "none",
            },
            "& .MuiDataGrid-virtualScroller": {
              backgroundColor: colors.primary[400],
            },
            "& .MuiDataGrid-footerContainer": {
              borderTop: "none",
              backgroundColor: colors.blueAccent[700],
            },
            "& .MuiCheckbox-root": {
              color: `${colors.greenAccent[200]} !important`,
            },
          }}
        >
          <DataGrid 
            checkboxSelection 
            rows={mockDataBookingTours}
            columns={columns}
          />
        </Box>
      </Box>
    );
  };
  
  export default TOUR;
  
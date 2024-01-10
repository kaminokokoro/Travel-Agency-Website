import {
  Box,
  Typography,
  useTheme,
} from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { tokens } from "../../../theme";
import { mockDataFlights } from "../../../data/mockData";
import Header from "../../../components/Header";

const Flight = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const columns = [
    { 
      field: "id",
      headerName: "ID" 
    },
    {
      field: "flightProvider",
      headerName: "Flight Provider",
      flex: 1,
      cellClassName: "name-column--cell",
    },
    {
      field: "flightCode",
      headerName: "Code",
      flex: 1,
    },
    {
      field: "flightOrigin",
      headerName: "Origin",
      flex: 1,
    },
    {
      field: "flightDestination",
      headerName: "Destination",
      flex: 1,
    },
    {
      field: "duration",
      headerName: "Duration",
      flex: 1,
    },
  ];

  return (
    <Box m="20px">
      <Header title="FLIGHTS SERVICE" subtitle="List of Flights" />
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
          rows={mockDataFlights}
          columns={columns}
        />
      </Box>
    </Box>
  );
};

export default Flight;

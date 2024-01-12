import {
    Box,
    Typography,
    useTheme,
  } from "@mui/material";
  import { DataGrid } from "@mui/x-data-grid";
  import { tokens } from "../../theme";
  import { mockUserData } from "../../data/mockData";
  import Header from "../../components/Header";
  
  const User = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    const columns = [
      { 
        field: "id",
        headerName: "ID" 
      },
      {
        field: "name",
        headerName: "Name",
        flex: 1,
        cellClassName: "name-column--cell",
      },
      {
        field: "phoneNumber",
        headerName: "Phone Number",
        flex: 1,
      },
      {
        field: "mail",
        headerName: "Mail",
        flex: 1,
        cellClassName: "name-column--cell",
      },
      {
        field: "authorize",
        headerName: "Authorize",
        flex: 1,
      }
    ];
  
    return (
      <Box m="20px">
        <Header title="Users" subtitle="User Management" />
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
            rows={mockUserData} 
            columns={columns}
          />
        </Box>
      </Box>
    );
  };
  
  export default User;
  
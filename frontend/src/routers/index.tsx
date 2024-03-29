import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Page } from "./types";
import ScrollToTop from "./ScrollToTop";
import Footer from "shared/Footer/Footer";
import PageHome from "containers/PageHome/PageHome";
import Page404 from "containers/Page404/Page404";
import ListingStayPage from "containers/ListingStayPage/ListingStayPage";
import HotelSaiGon from "containers/ListingStayPage/HotelSaiGon"; 
import HotelDanang from "containers/ListingStayPage/HotelDanang"; 
import HotelDalat from "containers/ListingStayPage/HotelDalat"; 
import HotelNhaTrang from "containers/ListingStayPage/HotelNhaTrang"; 
import HotelPhuquoc from "containers/ListingStayPage/HotelPhuquoc"; 
import HotelVungtau from "containers/ListingStayPage/HotelVungtau"; 
import HotelHalong from "containers/ListingStayPage/HotelHalong"; 
import HotelCantho from "containers/ListingStayPage/HotelCantho"; 
// import ListingStayMapPage from "containers/ListingStayPage/ListingStayMapPage";
import ListingExperiencesPage from "containers/ListingExperiencesPage/ListingExperiencesPage";
// import ListingExperiencesMapPage from "containers/ListingExperiencesPage/ListingExperiencesMapPage";
import CheckOutPage from "containers/CheckOutPage/CheckOutPage";
import PayPage from "containers/PayPage/PayPage";
import AccountPage from "containers/AccountPage/AccountPage";
import AccountPass from "containers/AccountPage/AccountPass";
import PageContact from "containers/PageContact/PageContact";
import PageAbout from "containers/PageAbout/PageAbout";
import PageSignUp from "containers/PageSignUp/PageSignUp";
import PageLogin from "containers/PageLogin/PageLogin";
// import PageAddListing1 from "containers/PageAddListing1/PageAddListing1";
// import PageAddListing2 from "containers/PageAddListing1/PageAddListing2";
// import PageAddListing3 from "containers/PageAddListing1/PageAddListing3";
// import PageAddListing4 from "containers/PageAddListing1/PageAddListing4";
// import PageAddListing5 from "containers/PageAddListing1/PageAddListing5";
// import PageAddListing6 from "containers/PageAddListing1/PageAddListing6";
// import PageAddListing7 from "containers/PageAddListing1/PageAddListing7";
// import PageAddListing8 from "containers/PageAddListing1/PageAddListing8";
// import PageAddListing9 from "containers/PageAddListing1/PageAddListing9";
// import PageAddListing10 from "containers/PageAddListing1/PageAddListing10";
import SiteHeader from "containers/SiteHeader";
import ListingFlightsPage from "containers/ListingFlightsPage/ListingFlightsPage";
import FooterNav from "components/FooterNav";
import useWindowSize from "hooks/useWindowResize";
import ListingStayDetailPage from "containers/ListingDetailPage/listing-stay-detail/ListingStayDetailPage";
import ListingExperiencesDetailPage from "containers/ListingDetailPage/listing-experiences-detail/ListingExperiencesDetailPage";

export const pages: Page[] = [
  { path: "/", exact: true, component: PageHome },
  { path: "/#", exact: true, component: PageHome },
  { path: "/home-1-header-2", exact: true, component: PageHome },
  //
  { path: "/listing-stay-hanoi", component: ListingStayPage },
  { path: "/listing-stay-tphcm", component: HotelSaiGon },
  { path: "/listing-stay-nhatrang", component: HotelNhaTrang },
  { path: "/listing-stay-cantho", component: HotelCantho },
  { path: "/listing-stay-dalat", component: HotelDalat },
  { path: "/listing-stay-vungtau", component: HotelVungtau },
  { path: "/listing-stay-halong", component: HotelHalong },
  { path: "/listing-stay-phuquoc", component: HotelPhuquoc },
  { path: "/listing-stay-danang", component: HotelDanang },
  // { path: "/listing-stay-map", component: ListingStayMapPage },



  { path: "/hotels/:id", component: ListingStayDetailPage },
  { path: "/listing-stay-detail", component: ListingStayDetailPage },
  //
  {
    path: "/listing-experiences",
    component: ListingExperiencesPage,
  },
  // {
  //   path: "/listing-experiences-map",
  //   component: ListingExperiencesMapPage,
  // },
  {
    path: "/listing-experiences-detail",
    component: ListingExperiencesDetailPage,
  },
  //
  //
  //
  { path: "/listing-flights", component: ListingFlightsPage },
  //
  { path: "/checkout", component: CheckOutPage },
  { path: "/pay-done", component: PayPage },
  //
  { path: "/account", component: AccountPage },
  { path: "/account-password", component: AccountPass },
  //
  //
  // { path: "/add-listing-1", component: PageAddListing1 },
  // { path: "/add-listing-2", component: PageAddListing2 },
  // { path: "/add-listing-3", component: PageAddListing3 },
  // { path: "/add-listing-4", component: PageAddListing4 },
  // { path: "/add-listing-5", component: PageAddListing5 },
  // { path: "/add-listing-6", component: PageAddListing6 },
  // { path: "/add-listing-7", component: PageAddListing7 },
  // { path: "/add-listing-8", component: PageAddListing8 },
  // { path: "/add-listing-9", component: PageAddListing9 },
  // { path: "/add-listing-10", component: PageAddListing10 },
  //
  { path: "/contact", component: PageContact },
  { path: "/about", component: PageAbout },
  { path: "/signup", component: PageSignUp },
  { path: "/login", component: PageLogin },
  { path: "/page404", component: Page404 },
  //
];

const MyRoutes = () => {
  let WIN_WIDTH = useWindowSize().width;
  if (typeof window !== "undefined") {
    WIN_WIDTH = WIN_WIDTH || window.innerWidth;
  }

  return (
    <BrowserRouter>
      <ScrollToTop />
      <SiteHeader />

      <Routes>
        {pages.map(({ component, path }) => {
          const Component = component;
          return <Route key={path} element={<Component />} path={path} />;
        })}
        <Route path="*" element={<Page404 />}/>
      </Routes>

      {WIN_WIDTH < 768 && <FooterNav />}
      <Footer />
    </BrowserRouter>
  );
};

export default MyRoutes;

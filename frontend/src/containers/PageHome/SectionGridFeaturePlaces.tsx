import React, { FC, ReactNode, useEffect, useState } from "react";
import { DEMO_STAY_LISTINGS } from "data/listings";
import { StayDataType, Hotel } from "data/types";
import ButtonPrimary from "shared/Button/ButtonPrimary";
import HeaderFilter from "./HeaderFilter";
import StayCard from "components/StayCard/StayCard";
import { Link } from "react-router-dom";
import { Server, HotelProps } from "../../Sever";

const DEMO_DATA: StayDataType[] = DEMO_STAY_LISTINGS.filter((_, i) => i < 8);
const DEMO_DATA2: StayDataType[] = DEMO_STAY_LISTINGS.filter((_, i) => 8 <= i && i < 16);
const DEMO_DATA3: StayDataType[] = DEMO_STAY_LISTINGS.filter((_, i) => 16 <= i && i < 24);


interface GetDataProps {
  city: string;
}

function useFilteredHotel({ city }: GetDataProps) {
  const [hotels, setHotels] = useState<Hotel[] | undefined>(undefined);

  useEffect(() => {
    const fetchHotels = async () => {
      try {
        const hotelData = await new Server().getFilteredHotel(undefined, city, undefined, 1000000000000);
        setHotels(hotelData.hotel);
        // console.log(">>>test filtered", hotelData.hotel)
      } catch (error) {
        console.error("Error fetching hotels:", error);
      }
    };

    fetchHotels();
  }, [city]); // Đảm bảo hook được gọi lại khi tham số city thay đổi

  return hotels;
}

export interface SectionGridFeaturePlacesProps {
  stayListings?: StayDataType[];
  gridClass?: string;
  heading?: ReactNode;
  subHeading?: ReactNode;
  headingIsCenter?: boolean;
  tabs?: string[];
}

const SectionGridFeaturePlaces: FC<SectionGridFeaturePlacesProps> = ({
  gridClass = "",
  heading = "Khách sạn nổi bật",
  subHeading = "",
  headingIsCenter,
  tabs = ["TP. Hồ Chí Minh", "Hà Nội", "Đà Nẵng"],
}) => {

  const [hotels, setHotels] = React.useState<Hotel[]>();

  useEffect(() => {
    const fetchHotels = async () => {
      try {
        const hotelData = await new Server().getAllHotel();
        setHotels(hotelData.hotel);
      } catch (error) {
        console.error("Error fetching hotels:", error);
      }
    };

    fetchHotels();
  }, []);

  // if (hotels && hotels.length > 0) {
  //   console.log(hotels[0].address);
  // } else {
  //   console.warn("Hotels data is not available or the array is empty.");
  // }

  const [stayListings, setStayListings] = useState<StayDataType[]>(DEMO_DATA);
  const [activeTab, setActiveTab] = useState("TP. Hồ Chí Minh");

  const renderCard = (stay: StayDataType) => {
    return <StayCard key={stay.id} data={stay} />;
  };

  const onClickTab = (tab: string) => {
    setActiveTab(tab);

    // Update stayListings based on the selected tab
    switch (tab) {
      case "TP. Hồ Chí Minh":
        setStayListings(DEMO_DATA);
        break;
      case "Hà Nội":
        setStayListings(DEMO_DATA2);
        break;
      case "Đà Nẵng":
        setStayListings(DEMO_DATA3);
        break;
      // Add cases for other tabs if needed
      default:
        setStayListings([]);
    }
  };

  return (
    <div className="nc-SectionGridFeaturePlaces relative">
      <HeaderFilter
        tabActive={activeTab}
        subHeading={subHeading}
        tabs={tabs}
        heading={heading}
        onClickTab={onClickTab}
      />
      <div
        className={`grid gap-6 md:gap-8 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 ${gridClass}`}
      >
        {stayListings.map((stay) => renderCard(stay))}
      </div>
      <div className="flex mt-16 justify-center items-center">
        {/* <Link to="/listing-stay">
          <ButtonPrimary>Show me more</ButtonPrimary>
        </Link> */}
      </div>
      {hotels && hotels.length > 0 ? (
        hotels.map((hotel) => (
          <div key={hotel.id}>
            <span>{hotel.rating_count} địa chỉ: </span>
            <span>{hotel.address}</span>
            {/* Add other hotel properties as needed */}
          </div>
        ))
      ) : (
        <div>No hotels available</div>
      )}
    </div>
  );
};

export default SectionGridFeaturePlaces;


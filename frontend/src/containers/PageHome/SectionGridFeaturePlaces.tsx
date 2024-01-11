import React, { FC, ReactNode, useEffect, useState } from "react";
// import { DEMO_STAY_LISTINGS } from "data/listings";
import {  Hotel } from "data/types";
// import ButtonPrimary from "shared/Button/ButtonPrimary";
import HeaderFilter from "./HeaderFilter";
import StayCard from "components/StayCard/StayCard";
import { Link } from "react-router-dom";
import { Server, HotelProps } from "../../Sever";

// const DEMO_DATA: Hotel[] = DEMO_STAY_LISTINGS.filter((_, i) => i < 8);
// const DEMO_DATA2: Hotel[] = DEMO_STAY_LISTINGS.filter((_, i) => 8 <= i && i < 16);
// const DEMO_DATA3: Hotel[] = DEMO_STAY_LISTINGS.filter((_, i) => 16 <= i && i < 24);


interface GetDataProps {
  city: string;
}

function useFilteredHotel({ city }: GetDataProps) {
  const [hotels, setHotels] = useState<Hotel[] | undefined>(undefined);

  useEffect(() => {
    const fetchHotels = async () => {
      try {
        const hotelData = await new Server().getFilteredHotel(undefined, city, undefined, 1000000000000);
        const hotelsWithGallery = hotelData.hotel.map((hotel) => ({
          ...hotel,
          galleryImgs: [
            "https://images.pexels.com/photos/1268871/pexels-photo-1268871.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
            "https://images.pexels.com/photos/1179156/pexels-photo-1179156.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
            "https://images.pexels.com/photos/2506988/pexels-photo-2506988.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
            "https://images.pexels.com/photos/2373201/pexels-photo-2373201.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
          ],
        }));
        setHotels(hotelsWithGallery);
        // console.log(hotelsWithGallery);
      } catch (error) {
        console.error("Error fetching hotels:", error);
      }
    };

    fetchHotels();
  }, [city]);

  return hotels;
}

export interface SectionGridFeaturePlacesProps {
  stayListings?: Hotel[];
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
  const hotels_hanoi = useFilteredHotel({ city: 'hà nội' });
  const hotels_danang = useFilteredHotel({ city: 'đà nẵng'});
  const hotels_tphcm = useFilteredHotel({ city: 'thành phố hồ chí minh'});

  const [stayListings, setStayListings] = useState<Hotel[]>([]);

  useEffect(() => {
    if (hotels_tphcm && hotels_tphcm.length > 0) {
      setStayListings(hotels_tphcm);
    }
  }, [hotels_tphcm]);

  const [activeTab, setActiveTab] = useState("TP. Hồ Chí Minh");

  const renderCard = (stay: Hotel) => {
    return <StayCard key={stay.id} data={stay} />;
  };

  const handleTabData = (tab: string, hotels: Hotel[] | undefined) => {
    setActiveTab(tab);
    if (hotels) {
      setStayListings(hotels);
    } else {
      console.warn(`Hotels data for ${tab} is not available or the array is empty.`);
    }
  };

  const onClickTab = (tab: string) => {
    switch (tab) {
      case "TP. Hồ Chí Minh":
        handleTabData(tab, hotels_tphcm);
        break;
      case "Hà Nội":
        handleTabData(tab, hotels_hanoi);
        break;
      case "Đà Nẵng":
        handleTabData(tab, hotels_danang);
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
    </div>
  );
};

export default SectionGridFeaturePlaces;

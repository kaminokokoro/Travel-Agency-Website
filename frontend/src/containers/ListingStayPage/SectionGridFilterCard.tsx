import React, { FC, useEffect, useState } from "react";
import StayCard from "components/StayCard/StayCard";
import { DEMO_STAY_LISTINGS } from "data/listings";
import { Hotel } from "data/types";
import Pagination from "shared/Pagination/Pagination";
import TabFilters from "./TabFilters";
import Heading2 from "components/Heading/Heading2";
import { Server } from "../../Sever";


export interface SectionGridFilterCardProps {
  className?: string;
  data?: Hotel[];
  name?: string;
}

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

const DEMO_DATA: Hotel[] = DEMO_STAY_LISTINGS.filter((_, i) => i < 8);
// const DEMO_DATA: StayDataType[] = DEMO_STAY_LISTINGS
// const DEMO_DATA2: StayDataType[] = DEMO_STAY_LISTINGS.filter((_, i) => i <= 8 && i < 8);

const SectionGridFilterCard: FC<SectionGridFilterCardProps> = ({
  className = "",
  name = "Hà Nội"
}) => {
  const [data, setData] = useState<Hotel[] | undefined>(undefined);
  const hotels_hanoi = useFilteredHotel({ city: name });

  useEffect(() => {
    setData(hotels_hanoi); // Cập nhật data khi hotels_hanoi thay đổi
  }, [hotels_hanoi]);
  return (
    <div
      className={`nc-SectionGridFilterCard ${className}`}
      data-nc-id="SectionGridFilterCard"
    >
      <Heading2 khachsan={data?.length} heading={name}/>

      <div className="mb-8 lg:mb-11">
        <TabFilters />
      </div>
      {
        data && data.length > 0 && (
          <div className="grid grid-cols-1 gap-6 md:gap-8 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
            {data.map((stay) => (
              <StayCard key={stay.id} data={stay} />
            ))}
          </div>
        )
      }
      {/* <div className="flex mt-16 justify-center items-center">
        <Pagination />
      </div> */}
    </div>
  );
};

export default SectionGridFilterCard;

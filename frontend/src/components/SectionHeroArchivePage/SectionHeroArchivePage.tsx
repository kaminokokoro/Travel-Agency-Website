import React, { FC, ReactNode, useEffect, useState } from "react";
import hanoi from "images/Hà Nội.png";
import tphcm from "images/tphcm.png";
import dalat from "images/dalat.png";
import nhatrang from "images/nhatrang.png";
import danang from "images/danang.png";
import cantho from "images/cantho.png";
import vungtau from "images/vungtau.png";
import halong from "images/halong.png";
import phuquoc from "images/phuquoc.png";
import HeroSearchForm, {
  SearchTab,
} from "components/HeroSearchForm/HeroSearchForm";
import { Server, HotelProps } from "../../Sever";
import { StayDataType, Hotel } from "data/types";


export interface SectionHeroArchivePageProps {
  className?: string;
  listingType?: ReactNode;
  currentPage: "Stays" | "Experiences" | "Flights";
  currentTab: SearchTab;
  rightImage?: string;
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
        const hotelData = await new Server().getFilteredHotel(undefined, city, undefined, 10000000);
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

const SectionHeroArchivePage: FC<SectionHeroArchivePageProps> = ({
  className = "",
  listingType,
  currentPage,
  currentTab,
  name
}) => {

  const [rightImage, setRightImage] = useState<string>(hanoi);
  const data = useFilteredHotel({ city: `${name}` });

  useEffect(() => {
    // Kiểm tra data.city và cập nhật rightImage tương ứng
    if (data && data.length >= 0) {
      switch (name) {
        case "Hà Nội":
          setRightImage(hanoi);
          break;
        case "Thành phố Hồ Chí Minh":
          setRightImage(tphcm);
          break;
        case "Đà Lạt":
          setRightImage(dalat);
          break;
        case "Đà Nẵng":
          setRightImage(danang);
          break;
        case "Nha Trang":
          setRightImage(nhatrang);
          break;
        case "Cần Thơ":
          setRightImage(cantho);
          break;
        case "Hạ Long":
          setRightImage(halong);
          break;
        case "Vũng Tàu":
          setRightImage(vungtau);
          break;
        case "Phú Quốc":
          setRightImage(phuquoc);
          break;
        // Thêm các case khác nếu có nhiều thành phố khác
        default:
          setRightImage(hanoi); // Giá trị mặc định khi không khớp city nào
      }
    }
  }, [data]);

  return (
    <div
      className={`nc-SectionHeroArchivePage flex flex-col relative ${className}`}
      data-nc-id="SectionHeroArchivePage"
    >
      {data && data.length >= 0 && (
        <div className="flex flex-col lg:flex-row lg:items-center">
          <div className="flex-shrink-0 lg:w-1/2 flex flex-col items-start space-y-6 lg:space-y-10 pb-14 lg:pb-64 xl:pb-80 xl:pr-14 lg:mr-10 xl:mr-0">
            <h2 className="font-medium text-4xl md:text-5xl xl:text-7xl leading-[110%]">
              {name}
            </h2>
            <div className="flex items-center text-base md:text-lg text-neutral-500 dark:text-neutral-400">
              <i className="text-2xl las la-map-marked"></i>
              <span className="ml-2.5">Việt Nam </span>
              <span className="mx-5">{data.length} khách sạn</span>
              {listingType ? (
                listingType
              ) : (
                <>
                  <i className="text-2xl las la-home"></i>
                  <span className="ml-2.5"></span>
                </>
              )}
            </div>
          </div>
          <div className="flex-grow">
            <img className="w-full" src={rightImage} alt="hero" />
          </div>
        </div>
      )}

      <div className="hidden lg:flow-root w-full">
        <div className="z-10 lg:-mt-40 xl:-mt-56 w-full">
          <HeroSearchForm currentPage={currentPage} currentTab={currentTab} />
        </div>
      </div>
    </div>
  );
};

export default SectionHeroArchivePage;

import BackgroundSection from "components/BackgroundSection/BackgroundSection";
import BgGlassmorphism from "components/BgGlassmorphism/BgGlassmorphism";
import SectionHeroArchivePage from "components/SectionHeroArchivePage/SectionHeroArchivePage";
import SectionSliderNewCategories from "components/SectionSliderNewCategories/SectionSliderNewCategories";
// import SectionSubscribe2 from "components/SectionSubscribe2/SectionSubscribe2";
import React, { FC, useEffect, useState } from "react";
import SectionGridFilterCard from "./SectionGridFilterCard";
import { Helmet } from "react-helmet";
import { Server, HotelProps } from "../../Sever";
import { StayDataType, Hotel } from "data/types";
import { TaxonomyType } from "data/types";


export interface ListingStayPageProps {
  className?: string;
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


const ListingStayPage: FC<ListingStayPageProps> = ({ className = "" }) => {
  
  const hotels_hanoi = useFilteredHotel({ city: 'hà nội' });
  const hotels_danang = useFilteredHotel({ city: 'đà nẵng'});
  const hotels_tphcm = useFilteredHotel({ city: 'thành phố hồ chí minh'});
  const hotels_nhatrang = useFilteredHotel({ city: 'nha trang'});
  const hotels_dalat = useFilteredHotel({ city: 'đà lạt'});
  const hotels_phuquoc = useFilteredHotel({ city: 'phú quốc'});
  const hotels_vungtau = useFilteredHotel({ city: 'vũng tàu'});
  const hotels_halong = useFilteredHotel({ city: 'hạ long'});
  const hotels_cantho = useFilteredHotel({ city: 'cần thơ'});


  const DEMO_CATS: TaxonomyType[] = [
    {
      id: "1",
      href: "/listing-stay-tphcm",
      name: "TP. Hồ Chí Minh",
      count: hotels_tphcm?.length,
      thumbnail:
        "https://viethouse.com.vn/wp-content/uploads/2021/07/3-toa-thap-bieu-tuong-cua-sai-gon-hien-dai-2_f_improf_500x750.jpg",
    },
    {
      id: "2",
      href: "/listing-stay-hanoi",
      name: "Hà Nội",
      count: hotels_hanoi?.length,
      thumbnail:
        "https://i.pinimg.com/564x/51/13/92/511392460f64504c9958190495a309b1.jpg",
    },
    {
      id: "3",
      href: "/listing-stay-danang",
      name: "Đà Nẵng",
      count: hotels_danang?.length,
      thumbnail:
        "https://i.pinimg.com/564x/d3/5d/04/d35d04cf1ea3741763a94415f3122222.jpg",
    },
    {
      id: "4",
      href: "/listing-stay-nhatrang",
      name: "Nha Trang",
      count: hotels_nhatrang?.length,
      thumbnail:
        "https://i.pinimg.com/564x/ae/38/d5/ae38d5828dd70d857e932d0467570a91.jpg",
    },
    {
      id: "5",
      href: "/listing-stay-dalat",
      name: "Đà Lạt",
      count: hotels_dalat?.length,
      thumbnail:
        "https://i.pinimg.com/564x/e4/21/a5/e421a526501edd8b4c2f515b7fe7961a.jpg",
    },
    {
      id: "7",
      href: "/listing-stay-phuquoc",
      name: "Đảo Phú Quốc",
      count: hotels_phuquoc?.length,
      thumbnail:
        "https://i.pinimg.com/564x/bc/d3/4e/bcd34e445d3b1ec8aefd2b5e37c6e46d.jpg",
    },
    {
      id: "8",
      href: "/listing-stay-vungtau",
      name: "Vũng Tàu",
      count: hotels_vungtau?.length,
      thumbnail:
        "https://i.pinimg.com/564x/94/08/2e/94082e6b8c08131855df8ca5c1e76460.jpg",
    },

    {
      id: "10",
      href: "/listing-stay-cantho",
      name: "Cần Thơ",
      count: hotels_cantho?.length,
      thumbnail:
        "https://i.pinimg.com/564x/4d/a2/8f/4da28f462a980325db0b2031cc7ff64b.jpg",
    },
  ];

  return (
    <div
      className={`nc-ListingStayPage relative overflow-hidden ${className}`}
      data-nc-id="ListingStayPage"
    >
      <Helmet>
        <title>Explore</title>
      </Helmet>
      <BgGlassmorphism />

      <div className="container relative overflow-hidden">
        {/* SECTION HERO */}
        <SectionHeroArchivePage
          currentPage="Stays"
          currentTab="Stays"
          className="pt-10 pb-24 lg:pb-28 lg:pt-16 "
          name="Hạ Long"
        />

        {/* SECTION */}
        <SectionGridFilterCard className="pb-24 lg:pb-28" name="Hạ Long"/>

        {/* SECTION 1 */}
        <div className="relative py-16">
          <BackgroundSection />
          <SectionSliderNewCategories
            heading="Khám phá các thành phố phổ biến của Việt Nam"
            subHeading=""
            categoryCardType="card5"
            itemPerRow={5}
            sliderStyle="style2"
            uniqueClassName="ListingStayMapPage"
            categories = {DEMO_CATS}
          />
        </div>

        {/* SECTION */}
        {/* <SectionSubscribe2 className="py-24 lg:py-28" /> */}
      </div>
    </div>
  );
};

export default ListingStayPage;

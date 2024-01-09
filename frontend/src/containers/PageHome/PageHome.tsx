import SectionHero from "components/SectionHero/SectionHero";
import SectionSliderNewCategories from "components/SectionSliderNewCategories/SectionSliderNewCategories";
import React from "react";
import SectionSubscribe2 from "components/SectionSubscribe2/SectionSubscribe2";
// import SectionOurFeatures from "components/SectionOurFeatures/SectionOurFeatures";
import SectionGridFeaturePlaces from "./SectionGridFeaturePlaces";
import BackgroundSection from "components/BackgroundSection/BackgroundSection";
import BgGlassmorphism from "components/BgGlassmorphism/BgGlassmorphism";
import { TaxonomyType } from "data/types";

const DEMO_CATS: TaxonomyType[] = [
  {
    id: "1",
    href: "/listing-stay",
    name: "TP. Hồ Chí Minh",
    count: 188288,
    thumbnail:
      "https://viethouse.com.vn/wp-content/uploads/2021/07/3-toa-thap-bieu-tuong-cua-sai-gon-hien-dai-2_f_improf_500x750.jpg",
  },
  {
    id: "2",
    href: "/listing-stay",
    name: "Hà Nội",
    count: 188288,
    thumbnail:
      "https://i.pinimg.com/564x/51/13/92/511392460f64504c9958190495a309b1.jpg",
  },
  {
    id: "3",
    href: "/listing-stay",
    name: "Đà Nẵng",
    count: 188288,
    thumbnail:
      "https://i.pinimg.com/564x/d3/5d/04/d35d04cf1ea3741763a94415f3122222.jpg",
  },
  {
    id: "4",
    href: "/listing-stay",
    name: "Nha Trang",
    count: 188288,
    thumbnail:
      "https://i.pinimg.com/564x/ae/38/d5/ae38d5828dd70d857e932d0467570a91.jpg",
  },
  {
    id: "5",
    href: "/listing-stay",
    name: "Đà Lạt",
    count: 188288,
    thumbnail:
      "https://i.pinimg.com/564x/e4/21/a5/e421a526501edd8b4c2f515b7fe7961a.jpg",
  },
  {
    id: "7",
    href: "/listing-stay",
    name: "Đảo Phú Quốc",
    count: 188288,
    thumbnail:
      "https://i.pinimg.com/564x/bc/d3/4e/bcd34e445d3b1ec8aefd2b5e37c6e46d.jpg",
  },
  {
    id: "8",
    href: "/listing-stay",
    name: "Vũng Tàu",
    count: 188288,
    thumbnail:
      "https://i.pinimg.com/564x/94/08/2e/94082e6b8c08131855df8ca5c1e76460.jpg",
  },
  {
    id: "9",
    href: "/listing-stay",
    name: "Hạ Long",
    count: 188288,
    thumbnail:
      "https://i.pinimg.com/564x/1f/9d/f2/1f9df2901739a49cd2aaec8206aefb15.jpg",
  },
  {
    id: "10",
    href: "/listing-stay",
    name: "Cần Thơ",
    count: 188288,
    thumbnail:
      "https://i.pinimg.com/564x/4d/a2/8f/4da28f462a980325db0b2031cc7ff64b.jpg",
  },
];

const DEMO_CATS_2: TaxonomyType[] = [
  {
    id: "1",
    href: "/listing-stay",
    name: "Enjoy the great cold",
    // taxonomy: "category",
    count: 188288,
    thumbnail:
      "https://images.pexels.com/photos/5764100/pexels-photo-5764100.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260",
  },
  {
    id: "222",
    href: "/listing-stay",
    name: "Sleep in a floating way",
    // taxonomy: "category",
    count: 188288,
    thumbnail:
      "https://images.pexels.com/photos/2869499/pexels-photo-2869499.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
  },
  {
    id: "3",
    href: "/listing-stay",
    name: "In the billionaire's house",
    // taxonomy: "category",
    count: 188288,
    thumbnail:
      "https://images.pexels.com/photos/7031413/pexels-photo-7031413.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
  },
  {
    id: "4",
    href: "/listing-stay",
    name: "Cool in the deep forest",
    // taxonomy: "category",
    count: 188288,
    thumbnail:
      "https://images.pexels.com/photos/247532/pexels-photo-247532.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
  },
  {
    id: "5",
    href: "/listing-stay",
    name: "In the billionaire's house",
    // taxonomy: "category",
    count: 188288,
    thumbnail:
      "https://images.pexels.com/photos/7031413/pexels-photo-7031413.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
  },
];


function PageHome() {


  return (
    <div className="nc-PageHome relative overflow-hidden">
      {/* GLASSMOPHIN */}
      <BgGlassmorphism />

      <div className="container relative space-y-24 mb-24 lg:space-y-28 lg:mb-28">
        {/* SECTION HERO */}
        <SectionHero className="pt-10 lg:pt-16 lg:pb-16" />

        {/* SECTION 1 */}
        <SectionSliderNewCategories
          heading = "Thành phố phổ biến tại Việt Nam"
          subHeading = ""
          categories={DEMO_CATS}
          uniqueClassName="PageHome_s1"
        />

        {/* SECTION2 */}
        {/* <SectionOurFeatures /> */}

        {/* SECTION */}
        <div className="relative py-16">
          <BackgroundSection />
          <SectionGridFeaturePlaces />
        </div>


        {/* SECTION 1 */}
        <div className="relative py-16">
          <BackgroundSection className="bg-orange-50 dark:bg-black dark:bg-opacity-20 " />
          <SectionSliderNewCategories
            categories={DEMO_CATS_2}
            categoryCardType="card4"
            itemPerRow={4}
            heading="Tour nổi bật"
            subHeading="Popular places to stay that Chisfis recommends for you"
            sliderStyle="style2"
            uniqueClassName="PageHome_s2"
          />
        </div>

        <SectionSubscribe2 />

      </div>
    </div>
  );
}

export default PageHome;

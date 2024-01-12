import BackgroundSection from "components/BackgroundSection/BackgroundSection";
import BgGlassmorphism from "components/BgGlassmorphism/BgGlassmorphism";
import SectionHeroArchivePage from "components/SectionHeroArchivePage/SectionHeroArchivePage";
import SectionSliderNewCategories from "components/SectionSliderNewCategories/SectionSliderNewCategories";
import { TaxonomyType } from "data/types";
import React, { FC } from "react";
import SectionGridFilterCard from "./SectionGridFilterCard";
import { Helmet } from "react-helmet";

export interface ListingExperiencesPageProps {
  className?: string;
}

const DEMO_CATS: TaxonomyType[] = [
  {
    id: "1",
    href: "#",
    name: "Phú Quốc ",
    // taxonomy: "category",
    count: 2,
    thumbnail:
      "https://i.pinimg.com/564x/0e/d9/d9/0ed9d9a76e98822f56e3380d6f7dadee.jpg",
    listingType: "experiences",
  },
  {
    id: "2",
    href: "#",
    name: "Sapa - Lào Cai",
    // taxonomy: "category",
    count: 3,
    thumbnail:
      "https://i.pinimg.com/564x/c4/3c/42/c43c420d2d4956ab511be00f33066254.jpg",
    listingType: "experiences",
  },
  {
    id: "3",
    href: "#",
    name: "Đà Nẵng",
    // taxonomy: "category",
    count: 3,
    thumbnail:
      "https://i.pinimg.com/564x/58/bd/7c/58bd7c653d1fc5d227ca8fad58232b2a.jpg",
    listingType: "experiences",
  },
  {
    id: "5",
    href: "#",
    name: "Đà Lạt",
    // taxonomy: "category",
    count: 4,
    thumbnail:
      "https://i.pinimg.com/564x/1d/08/24/1d0824a14262b7063d5703c290805b0b.jpg",
    listingType: "experiences",
  },
];

const ListingExperiencesPage: FC<ListingExperiencesPageProps> = ({
  className = "",
}) => {
  return (
    <div
      className={`nc-ListingExperiencesPage relative overflow-hidden ${className}`}
      data-nc-id="ListingExperiencesPage"
    >
      <Helmet>
        <title>Explore</title>
      </Helmet>
      <BgGlassmorphism />

      <div className="container relative">
        {/* SECTION HERO */}
        <SectionHeroArchivePage
          currentPage="Experiences"
          currentTab="Experiences"
          name="Hà Nội"
          listingType={
            <>
              <i className="text-2xl las la-umbrella-beach"></i>
              <span className="ml-2.5">2 Tours</span>
            </>
          }
          className="pt-10 pb-24 lg:pb-28 lg:pt-16 "
        />

        {/* SECTION */}
        <SectionGridFilterCard className="pb-24 lg:pb-28" />

        {/* SECTION 1 */}
        <div className="relative py-16">
          <BackgroundSection />
          <SectionSliderNewCategories
            heading="Khám phá thêm các điểm du lịch tại Việt Nam ✈"
            subHeading="Hàng trăm Tour trên khắp đất nước"
            categoryCardType="card4"
            itemPerRow={4}
            categories={DEMO_CATS}
            sliderStyle="style2"
            uniqueClassName="ListingExperiencesPage"
          />
        </div>

        {/* SECTION */}
      </div>
    </div>
  );
};

export default ListingExperiencesPage;

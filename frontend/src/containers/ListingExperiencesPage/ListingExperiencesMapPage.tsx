import React, { FC } from "react";
import BackgroundSection from "components/BackgroundSection/BackgroundSection";
import BgGlassmorphism from "components/BgGlassmorphism/BgGlassmorphism";
import SectionHeroArchivePage from "components/SectionHeroArchivePage/SectionHeroArchivePage";
import SectionSliderNewCategories from "components/SectionSliderNewCategories/SectionSliderNewCategories";
import SectionSubscribe2 from "components/SectionSubscribe2/SectionSubscribe2";
import SectionGridHasMap from "./SectionGridHasMap";
import { Helmet } from "react-helmet";

export interface ListingExperiencesMapPageProps {
  className?: string;
}

const ListingExperiencesMapPage: FC<ListingExperiencesMapPageProps> = ({
  className = "",
}) => {
  return (
    <div
      className={`nc-ListingExperiencesMapPage relative ${className}`}
      data-nc-id="ListingExperiencesMapPage"
    >
      <Helmet>
        <title>LU</title>
      </Helmet>
      <BgGlassmorphism />

      {/* SECTION HERO */}
      <div className="container pt-10 pb-24 lg:pt-16 lg:pb-28">
        <SectionHeroArchivePage
          currentPage="Experiences"
          currentTab="Experiences"
          listingType={
            <>
              <i className="text-2xl las la-umbrella-beach"></i>
              <span className="ml-2.5">1599 experiences</span>
            </>
          }
        />
      </div>

      {/* SECTION */}
      <div className="container pb-24 lg:pb-28 2xl:pl-10 xl:pr-0 xl:max-w-none">
        <SectionGridHasMap />
      </div>

      <div className="container overflow-hidden">
        {/* SECTION 1 */}
        <div className="relative py-16">
          <BackgroundSection />
          <SectionSliderNewCategories
            heading="Explore by types of stays"
            subHeading="Explore houses based on 10 types of stays"
            categoryCardType="card5"
            itemPerRow={5}
            sliderStyle="style2"
            uniqueClassName="ListingExperiencesMapPage"
          />
        </div>

        {/* SECTION */}
        <SectionSubscribe2 className="py-24 lg:py-28" />
      </div>
    </div>
  );
};

export default ListingExperiencesMapPage;

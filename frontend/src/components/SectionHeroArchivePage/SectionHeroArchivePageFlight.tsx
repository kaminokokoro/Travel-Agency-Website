import React, { FC, ReactNode, useEffect, useState } from "react";
import maybay from "images/maybay.png"

import HeroSearchForm, {
  SearchTab,
} from "components/HeroSearchForm/HeroSearchForm";
import { Server } from "../../Sever";


export interface SectionHeroArchivePageProps {
  className?: string;
  listingType?: ReactNode;
  currentPage: "Stays" | "Experiences" | "Flights";
  currentTab: SearchTab;
  rightImage?: string;
  name?: string;
}


const SectionHeroArchivePageFlight: FC<SectionHeroArchivePageProps> = ({
  className = "",
  listingType,
  currentPage,
  currentTab,
  name
}) => {

  const [rightImage, setRightImage] = useState<string>(maybay);

  return (
    <div
      className={`nc-SectionHeroArchivePage flex flex-col relative ${className}`}
      data-nc-id="SectionHeroArchivePage"
    >
        <div className="flex flex-col lg:flex-row lg:items-center">
        <div className="flex-shrink-0 lg:w-1/2 flex flex-col items-start space-y-6 lg:space-y-10 pb-14 lg:pb-64 xl:pb-80 xl:pr-14 lg:mr-10 xl:mr-0">
          <h2 className="font-medium text-4xl md:text-5xl xl:text-7xl leading-[110%]">
            Chuyến bay
          </h2>
          <div className="flex items-center text-base md:text-lg text-neutral-500 dark:text-neutral-400">
            <i className="text-2xl las la-map-marked"></i>
            <span className="ml-2.5">Việt Nam </span>
            <span className="mx-5"></span>
            {listingType ? (
              listingType
            ) : (
              <>
                <i className="text-2xl las la-home"></i>
              </>
            )}
          </div>
        </div>
        <div className="flex-grow">
          <img className="w-full" src={rightImage} alt="hero" />
        </div>
      </div>

      <div className="hidden lg:flow-root w-full">
        <div className="z-10 lg:-mt-40 xl:-mt-56 w-full">
          <HeroSearchForm currentPage={currentPage} currentTab={currentTab} />
        </div>
      </div>
    </div>
  );
};

export default SectionHeroArchivePageFlight;

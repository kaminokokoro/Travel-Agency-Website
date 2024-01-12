import React, { FC } from "react";
import { ArrowRightIcon, Squares2X2Icon } from "@heroicons/react/24/outline";
import CommentListing from "components/CommentListing/CommentListing";
import FiveStartIconForRate from "components/FiveStartIconForRate/FiveStartIconForRate";
import StartRating from "components/StartRating/StartRating";
import { useLocation, useNavigate } from "react-router-dom";
import ButtonSecondary from "shared/Button/ButtonSecondary";
import ButtonCircle from "shared/Button/ButtonCircle";
import Input from "shared/Input/Input";
import ButtonPrimary from "shared/Button/ButtonPrimary";
import DetailPagetLayout from "../Layout";
import { PHOTOS } from "./constant";
import StayDatesRangeInput from "./StayDatesRangeInput";
import GuestsInput from "./GuestsInput";

const ListingExperiencesDetail: FC<{}> = () => {
  const thisPathname = useLocation().pathname;
  const router = useNavigate();

  const handleOpenModalImageGallery = () => {
    router(`${thisPathname}/?modal=PHOTO_TOUR_SCROLLABLE`);
  };

  const renderSection1 = () => {
    return (
      <div className="listingSection__wrap !space-y-6">

        {/* 2 */}
        <h2 className="text-2xl sm:text-3xl lg:text-4xl font-semibold">
          Trang An Boat Tour & Mua Cave
        </h2>

        {/* 3 */}
        <div className="flex items-center space-x-4">
          <StartRating />
          <span>·</span>
          <span>
            <i className="las la-map-marker-alt"></i>
            <span className="ml-1"> Hà Nội</span>
          </span>
        </div>


      </div>
    );
  };

  const renderSection2 = () => {
    return (
      <div className="listingSection__wrap">
        <h2 className="text-2xl font-semibold">Mô tả tour</h2>
        <div className="w-14 border-b border-neutral-200 dark:border-neutral-700"></div>
        <div className="text-neutral-6000 dark:text-neutral-300">
        </div>
      </div>
    );
  };

  const renderSection6 = () => {
    return (
      <div className="listingSection__wrap">
        {/* HEADING */}
        <h2 className="text-2xl font-semibold">Đánh giá (2 đánh giá)</h2>
        <div className="w-14 border-b border-neutral-200 dark:border-neutral-700"></div>

        {/* Content */}
        <div className="space-y-5">
          <FiveStartIconForRate iconClass="w-6 h-6" className="space-x-0.5" />
          <div className="relative">
            <Input
              fontClass=""
              sizeClass="h-16 px-4 py-3"
              rounded="rounded-3xl"
              placeholder="Chia sẻ cảm nhận của bạn..."
            />
            <ButtonCircle
              className="absolute right-2 top-1/2 transform -translate-y-1/2"
              size=" w-12 h-12 "
            >
              <ArrowRightIcon className="w-5 h-5" />
            </ButtonCircle>
          </div>
        </div>

        {/* comment */}
        <div className="divide-y divide-neutral-100 dark:divide-neutral-800">
          <CommentListing className="py-8" />
          <CommentListing className="py-8" />
        </div>
      </div>
    );
  };

  const renderSection8 = () => {
    return (
      <div className="listingSection__wrap">
        {/* HEADING */}
        <h2 className="text-2xl font-semibold">Lưu ý</h2>
        <div className="w-14 border-b border-neutral-200 dark:border-neutral-700" />

        {/* CONTENT */}
        <div>
          <h4 className="text-lg font-semibold">Chính sách hủy Tour</h4>
          <span className="block mt-3 text-neutral-500 dark:text-neutral-400">
          Mọi tour đều có thể bị hủy và được hoàn tiền đầy đủ trong vòng 24 giờ kể từ khi mua hoặc ít nhất 7 ngày trước khi tour bắt đầu
          </span>
        </div>
        <div className="w-14 border-b border-neutral-200 dark:border-neutral-700" />
      </div>
    );
  };

  const renderSidebar = () => {
    return (
      <div className="listingSectionSidebar__wrap shadow-xl">
        {/* PRICE */}
        <div className="flex justify-between">
          <span className="text-3xl font-semibold">
            200000 VND 
            <span className="ml-1 text-base font-normal text-neutral-500 dark:text-neutral-400">
              /người
            </span>
          </span>
          <StartRating />
        </div>

        {/* FORM */}
        {/* FORM */}
        <form className="flex flex-col border border-neutral-200 dark:border-neutral-700 rounded-3xl ">
          {/* <StayDatesRangeInput className="flex-1 z-[11]" /> */}
          {/* <div className="w-full border-b border-neutral-200 dark:border-neutral-700"></div> */}
          <GuestsInput className="flex-1" />
        </form>

        {/* SUM */}
        <div className="flex flex-col space-y-4">
          <div className="flex justify-between text-neutral-6000 dark:text-neutral-300">
            <span>200000 VND x 4 người</span>
            <span>800000 VND</span>
          </div>
          <div className="border-b border-neutral-200 dark:border-neutral-700"></div>
          <div className="flex justify-between font-semibold">
            <span>Tổng</span>
            <span>800000 VND</span>
          </div>
        </div>

        {/* SUBMIT */}
        <ButtonPrimary href={"/checkout"}>Đặt trước</ButtonPrimary>
      </div>
    );
  };

  return (
    <div className={` nc-ListingExperiencesDetailPage `}>
      {/* SINGLE HEADER */}
      <header className="rounded-md sm:rounded-xl">
        <div className="relative grid grid-cols-4 gap-1 sm:gap-2">
          <div
            className="col-span-3 row-span-3 relative rounded-md sm:rounded-xl overflow-hidden cursor-pointer"
            onClick={handleOpenModalImageGallery}
          >
            <img
              alt="photos 1"
              className="absolute inset-0 object-cover rounded-md sm:rounded-xl w-full h-full"
              src={PHOTOS[0]}
              sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 50vw"
            />
            <div className="absolute inset-0 bg-neutral-900 bg-opacity-20 opacity-0 hover:opacity-100 transition-opacity"></div>
          </div>
          {PHOTOS.filter((_, i) => i >= 1 && i < 4).map((item, index) => (
            <div
              key={index}
              className={`relative rounded-md sm:rounded-xl overflow-hidden ${
                index >= 2 ? "block" : ""
              }`}
            >
              <div className="aspect-w-4 aspect-h-3">
                <img
                  alt="photos"
                  className="absolute inset-0 object-cover w-full h-full rounded-md sm:rounded-xl"
                  src={item || ""}
                  sizes="400px"
                />
              </div>

              {/* OVERLAY */}
              <div
                className="absolute inset-0 bg-neutral-900 bg-opacity-20 opacity-0 hover:opacity-100 transition-opacity cursor-pointer"
                onClick={handleOpenModalImageGallery}
              />
            </div>
          ))}

          <div
            className="absolute hidden md:flex md:items-center md:justify-center left-3 bottom-3 px-4 py-2 rounded-xl bg-neutral-100 text-neutral-500 cursor-pointer hover:bg-neutral-200 z-10"
            onClick={handleOpenModalImageGallery}
          >
            <Squares2X2Icon className="h-5 w-5" />
            <span className="ml-2 text-neutral-800 text-sm font-medium">
              Show all photos
            </span>
          </div>
        </div>
      </header>

      {/* MAIn */}
      <main className="relative z-10 mt-11 flex flex-col lg:flex-row ">
        {/* CONTENT */}
        <div className="w-full lg:w-3/5 xl:w-2/3 space-y-8 lg:pr-10 lg:space-y-10">
          {renderSection1()}
          {renderSection2()}
          {renderSection6()}
          {renderSection8()}
        </div>

        {/* SIDEBAR */}
        <div className="hidden lg:block flex-grow mt-14 lg:mt-0">
          <div className="sticky top-28">{renderSidebar()}</div>
        </div>
      </main>
    </div>
  );
};

export default function ListingExperiencesDetailPage() {
  return (
    <DetailPagetLayout>
      <ListingExperiencesDetail />
    </DetailPagetLayout>
  );
}

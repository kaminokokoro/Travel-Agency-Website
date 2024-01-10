import React, { FC, useEffect } from "react";
import CommentListing from "components/CommentListing/CommentListing";
import FiveStartIconForRate from "components/FiveStartIconForRate/FiveStartIconForRate";
import StartRating from "components/StartRating/StartRating";
import StayDatesRangeInput from "./StayDatesRangeInput";
import { useLocation, useNavigate } from "react-router-dom";
import { PHOTOS } from "./constant";
import { ArrowRightIcon, Squares2X2Icon } from "@heroicons/react/24/outline";
import ButtonSecondary from "shared/Button/ButtonSecondary";
import ButtonCircle from "shared/Button/ButtonCircle";
import Input from "shared/Input/Input";
import ButtonPrimary from "shared/Button/ButtonPrimary";
import DetailPagetLayout from "../Layout";
import GuestsInput from "./GuestsInput";
import { Hotel, HotelRatingByHotelId } from "data/types";
import { Server, HotelProps } from "../../../Sever";




const StayDetailPageContainer: FC<{}> = () => {
  //
  const location = useLocation();
  const id = location.pathname.split("/")[2];
  const [data, setData] = React.useState<Hotel | undefined>(undefined);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await new Server().getHotel(id);
        setData(result.hotel);
      } catch (error) {
        console.error("Error fetching hotel:", error);
      }
    };

    fetchData();
  }, [id]);

  const [hotelRating, setHotelRating] = React.useState<HotelRatingByHotelId[] | undefined>(undefined);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await new Server().getHotelRatingByHotelId(id);
        setHotelRating(result["Hotel Rating"]);
      } catch (error) {
        console.error("Error fetching hotel:", error);
      }
    };

    fetchData();
  }, [id]);

  const thisPathname = useLocation().pathname;
  const router = useNavigate();

  const handleOpenModalImageGallery = () => {
    router(`${thisPathname}/?modal=PHOTO_TOUR_SCROLLABLE`);
  };

  const renderSection1 = () => {
    return (
      <div className="listingSection__wrap !space-y-6">
        {data ? (
          <>
            <h2 className="text-2xl sm:text-3xl lg:text-4xl font-semibold">
              {data.name}
            </h2>
            <div className="flex items-center space-x-4">
              <StartRating
                point={data.average_rating}
                reviewCount={data.rating_count}
              />
              <span>·</span>
              <span>
                <i className="las la-map-marker-alt"></i>
                <span className="ml-1">{data.address}</span>
              </span>
            </div>
          </>
        ) : (
          // Placeholder hoặc xử lý khi data không tồn tại
          <p>Data is unavailable</p>
        )}

        <div className="w-full border-neutral-100 dark:border-neutral-700" />
      </div>
    );
  };

  const renderSection2 = () => {
    return (
      <div className="listingSection__wrap">
        <h2 className="text-2xl font-semibold">Thông tin khách sạn</h2>
        <div className="w-14 border-b border-neutral-200 dark:border-neutral-700"></div>
        {data ? (
          <div className="text-neutral-6000 dark:text-neutral-300">
            {data.description}
          </div>
        ) : (
          // Placeholder hoặc xử lý khi data không tồn tại
          <p>Data is unavailable</p>
        )}
      </div>
    );
  };


  const renderSection6 = () => {
    return (
      <div className="listingSection__wrap">
        {hotelRating ? (
          /* HEADING */
          <>
            <h2 className="text-2xl font-semibold">Đánh giá ({hotelRating.length || 0} đánh giá)</h2>
            <div className="w-14 border-b border-neutral-200 dark:border-neutral-700"></div>

            {/* Content */}
            <div className="space-y-5">
              <FiveStartIconForRate iconClass="w-6 h-6" className="space-x-0.5" />
              <div className="relative">
                <Input
                  fontClass=""
                  sizeClass="h-16 px-4 py-3"
                  rounded="rounded-3xl"
                  placeholder="Share your thoughts ..."
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
              <CommentListing className="py-8" />
              <CommentListing className="py-8" />
              {/* <div className="pt-8">
                <ButtonSecondary>View more 20 reviews</ButtonSecondary>
              </div> */}
            </div>
          </>
        ) : null}

      </div>
    );
  };


  const renderSection8 = () => {
    return (
      <div className="listingSection__wrap">
        {/* HEADING */}
        <h2 className="text-2xl font-semibold">Một số lưu ý</h2>
        <div className="w-14 border-b border-neutral-200 dark:border-neutral-700" />

        {/* CONTENT */}
        <div>
          <h4 className="text-lg font-semibold">Chính sách hủy thuê phòng</h4>
          <span className="block mt-3 text-neutral-500 dark:text-neutral-400">
            Hoàn tiền 50% giá trị đặt phòng khi khách hàng hủy phòng trong vòng 48 giờ
            sau khi đặt phòng thành công và 14 ngày trước thời gian nhận phòng. <br />
            Sau đó, hủy phòng trước 14 ngày so với giờ nhận phòng, được hoàn 50% tổng
            số tiền đã thanh toán (trừ phí dịch vụ).
          </span>
        </div>
        <div className="w-14 border-b border-neutral-200 dark:border-neutral-700" />

        {/* CONTENT */}
        <div>
          <h4 className="text-lg font-semibold">Giờ nhận phòng</h4>
          <div className="mt-3 text-neutral-500 dark:text-neutral-400 max-w-md text-sm sm:text-base">
            <div className="flex space-x-10 justify-between p-3 bg-neutral-100 dark:bg-neutral-800 rounded-lg">
              <span>Nhận phòng</span>
              <span>08:00 am - 12:00 am</span>
            </div>
            <div className="flex space-x-10 justify-between p-3">
              <span>Trả phòng</span>
              <span>02:00 pm - 04:00 pm</span>
            </div>
          </div>
        </div>
        <div className="w-14 border-b border-neutral-200 dark:border-neutral-700" />

        {/* CONTENT */}
        <div>
          <h4 className="text-lg font-semibold">Đặc biệt lưu ý</h4>
          <div className="prose sm:prose">
            <ul className="mt-3 text-neutral-500 dark:text-neutral-400 space-y-2">
              <li>
                Tôi và bạn sẽ cùng nhau giữ gìn cảnh quan, môi trường xanh, sạch bằng cách
                không xả rác, không sử dụng chất kích thích và tôn trọng mọi người xung quanh.
              </li>
              <li>Không hát karaoke quá 11h30.</li>
            </ul>
          </div>
        </div>
      </div>
    );
  };

  const renderSidebar = () => {
    return (
      <div className="listingSectionSidebar__wrap shadow-xl">
        {/* PRICE */}
        <div className="flex justify-between">
          <span className="text-3xl font-semibold">
            $119
            <span className="ml-1 text-base font-normal text-neutral-500 dark:text-neutral-400">
              /night
            </span>
          </span>
          <StartRating />
        </div>

        {/* FORM */}
        <form className="flex flex-col border border-neutral-200 dark:border-neutral-700 rounded-3xl ">
          <StayDatesRangeInput className="flex-1 z-[11]" />
          <div className="w-full border-b border-neutral-200 dark:border-neutral-700"></div>
          <GuestsInput className="flex-1" />
        </form>

        {/* SUM */}
        <div className="flex flex-col space-y-4">
          <div className="flex justify-between text-neutral-6000 dark:text-neutral-300">
            <span>$119 x 3 night</span>
            <span>$357</span>
          </div>
          <div className="flex justify-between text-neutral-6000 dark:text-neutral-300">
            <span>Service charge</span>
            <span>$0</span>
          </div>
          <div className="border-b border-neutral-200 dark:border-neutral-700"></div>
          <div className="flex justify-between font-semibold">
            <span>Total</span>
            <span>$199</span>
          </div>
        </div>

        {/* SUBMIT */}
        <ButtonPrimary href={"/checkout"}>Reserve</ButtonPrimary>
      </div>
    );
  };

  return (
    <div className="nc-ListingStayDetailPage">
      {/*  HEADER */}
      <header className="rounded-md sm:rounded-xl">
        <div className="relative grid grid-cols-3 sm:grid-cols-4 gap-1 sm:gap-2">
          <div
            className="col-span-2 row-span-3 sm:row-span-2 relative rounded-md sm:rounded-xl overflow-hidden cursor-pointer "
            onClick={handleOpenModalImageGallery}
          >
            <img
              className="absolute inset-0 object-cover rounded-md sm:rounded-xl w-full h-full"
              src={PHOTOS[0]}
              alt=""
              sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 50vw"
            />
            <div className="absolute inset-0 bg-neutral-900 bg-opacity-20 opacity-0 hover:opacity-100 transition-opacity"></div>
          </div>
          {PHOTOS.filter((_, i) => i >= 1 && i < 5).map((item, index) => (
            <div
              key={index}
              className={`relative rounded-md sm:rounded-xl overflow-hidden ${index >= 3 ? "hidden sm:block" : ""
                }`}
            >
              <div className="aspect-w-4 aspect-h-3 sm:aspect-w-6 sm:aspect-h-5">
                <img
                  className="absolute inset-0 object-cover rounded-md sm:rounded-xl w-full h-full"
                  src={item || ""}
                  alt=""
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

          <button
            className="absolute hidden md:flex md:items-center md:justify-center left-3 bottom-3 px-4 py-2 rounded-xl bg-neutral-100 text-neutral-500 hover:bg-neutral-200 z-10"
            onClick={handleOpenModalImageGallery}
          >
            <Squares2X2Icon className="w-5 h-5" />
            <span className="ml-2 text-neutral-800 text-sm font-medium">
              Show all photos
            </span>
          </button>
        </div>
      </header>

      {/* MAIN */}
      <main className=" relative z-10 mt-11 flex flex-col lg:flex-row ">
        {/* CONTENT */}
        <div className="w-full lg:w-3/5 xl:w-2/3 space-y-8 lg:space-y-10 lg:pr-10">
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

export default function ListingStayDetailPage() {
  return (
    <DetailPagetLayout>
      <StayDetailPageContainer />
    </DetailPagetLayout>
  );
}

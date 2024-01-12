import { Tab } from "@headlessui/react";
import React, { FC, Fragment } from "react";
import visaPng from "images/vis.png";
import mastercardPng from "images/mastercard.svg";
import StartRating from "components/StartRating/StartRating";
import Label from "components/Label/Label";
import Input from "shared/Input/Input";
import Textarea from "shared/Textarea/Textarea";
import ButtonPrimary from "shared/Button/ButtonPrimary";

export interface CheckOutPagePageMainProps {
  className?: string;
}

const CheckOutPagePageMain: FC<CheckOutPagePageMainProps> = ({
  className = "",
}) => {

  const renderSidebar = () => {
    return (
      <div className="w-full flex flex-col sm:rounded-2xl lg:border border-neutral-200 dark:border-neutral-700 space-y-6 sm:space-y-8 px-0 sm:p-6 xl:p-8">
        <div className="flex flex-col sm:flex-row sm:items-center">
          <div className="flex-shrink-0 w-full sm:w-40">
            <div className=" aspect-w-4 aspect-h-3 sm:aspect-h-4 rounded-2xl overflow-hidden">
              <img
                alt=""
                className="absolute inset-0 object-cover"
                sizes="200px"
                src="https://images.pexels.com/photos/6373478/pexels-photo-6373478.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
              />
            </div>
          </div>
          <div className="py-5 sm:px-5 space-y-3">
            <div>
              <span className="text-sm text-neutral-500 dark:text-neutral-400 line-clamp-1">
              Phòng Gia Đình
              </span>
              <span className="text-base font-medium mt-1 block">
                HUS Hotel
              </span>
            </div>
            {/* <span className="block  text-sm text-neutral-500 dark:text-neutral-400">
              2 beds · 2 baths
            </span> */}
            <div className="w-10 border-b border-neutral-200  dark:border-neutral-700"></div>
            <StartRating />
          </div>
        </div>
        <div className="flex flex-col space-y-4">
          <h3 className="text-2xl font-semibold">Giá chi tiết</h3>
          <div className="flex justify-between text-neutral-6000 dark:text-neutral-300">
            <span>400000 VNĐ x 3 ngày</span>
            <span>1200000 VNĐ</span>
          </div>
          {/* <div className="flex justify-between text-neutral-6000 dark:text-neutral-300">
            <span>Service charge</span>
            <span>$0</span>
          </div> */}

          <div className="border-b border-neutral-200 dark:border-neutral-700"></div>
          <div className="flex justify-between font-semibold">
            <span>Tổng</span>
            <span>1200000 VNĐ</span>
          </div>
        </div>
      </div>
    );
  };

  const renderMain = () => {
    return (
      <div className="w-full flex flex-col sm:rounded-2xl sm:border border-neutral-200 dark:border-neutral-700 space-y-8 px-0 sm:p-6 xl:p-8">
        <h2 className="text-3xl lg:text-4xl font-semibold">
          Xác nhận và thanh toán
        </h2>
        <div className="border-b border-neutral-200 dark:border-neutral-700"></div>

        <div>
          <h3 className="text-2xl font-semibold">Thanh toán bằng</h3>
          <div className="w-14 border-b border-neutral-200 dark:border-neutral-700 my-5"></div>

          <div className="mt-6">
            <Tab.Group>
              <Tab.List className="flex my-5 gap-1">
                <Tab as={Fragment}>
                  {({ selected }) => (
                    <button
                      className={`px-4 py-1.5 sm:px-6 sm:py-2.5  rounded-full flex items-center justify-center focus:outline-none  ${
                        selected
                          ? "bg-neutral-800 dark:bg-neutral-200 text-white dark:text-neutral-900"
                          : " text-neutral-6000 dark:text-neutral-400 hover:bg-neutral-100 dark:hover:bg-neutral-800"
                      }`}
                    >
                      <span className="mr-2.5">Credit card</span>
                      <img className="w-8" src={visaPng} alt="visa" />
                      <img
                        className="w-8"
                        src={mastercardPng}
                        alt="mastercard"
                      />
                    </button>
                  )}
                </Tab>
                <Tab as={Fragment}>
                  {({ selected }) => (
                    <button
                      className={`px-4 py-1.5 sm:px-6 sm:py-2.5 rounded-full focus:outline-none ${
                        selected
                          ? "bg-neutral-800 dark:bg-neutral-200 text-white dark:text-neutral-900"
                          : "text-neutral-6000 dark:text-neutral-400 hover:bg-neutral-100 dark:hover:bg-neutral-800"
                      }`}
                    >
                      Paypal
                    </button>
                  )}
                </Tab>
              </Tab.List>

              <Tab.Panels>
                <Tab.Panel className="space-y-5">
                  <div className="space-y-1">
                    <Label>Số thẻ </Label>
                    <Input defaultValue="" />
                  </div>
                  <div className="space-y-1">
                    <Label>Chủ thẻ </Label>
                    <Input defaultValue="" />
                  </div>
                  <div className="flex space-x-5  ">
                    <div className="flex-1 space-y-1">
                      <Label>Ngày hết hạn </Label>
                      <Input type="date" defaultValue="MM/YY" />
                    </div>
                    <div className="flex-1 space-y-1">
                      <Label>CVC </Label>
                      <Input />
                    </div>
                  </div>
                </Tab.Panel>
                <Tab.Panel className="space-y-5">
                  <div className="space-y-1">
                    <Label>Email </Label>
                    <Input type="email" defaultValue="" />
                  </div>
                  <div className="space-y-1">
                    <Label>Mật khẩu </Label>
                    <Input type="password" defaultValue="" />
                  </div>
                </Tab.Panel>
              </Tab.Panels>
            </Tab.Group>
            <div className="pt-8">
              <ButtonPrimary href={"/pay-done"}>Xác nhận và thanh toán</ButtonPrimary>
            </div>
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className={`nc-CheckOutPagePageMain ${className}`}>
      <main className="container mt-11 mb-24 lg:mb-32 flex flex-col-reverse lg:flex-row">
        <div className="w-full lg:w-3/5 xl:w-2/3 lg:pr-10 ">{renderMain()}</div>
        <div className="hidden lg:block flex-grow">{renderSidebar()}</div>
      </main>
    </div>
  );
};

export default CheckOutPagePageMain;

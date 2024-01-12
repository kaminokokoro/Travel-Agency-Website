import React, { FC, useState } from "react";

export interface FlightCardProps {
  className?: string;
  defaultOpen?: boolean;
  data: {
    id: string;
    departure_date: string;
    arrival_date: string;
    departure_from: string;
    arrival_to: string;
    ten_may_bay: string;
    airlines: {
      logo: string;
      name: string;
    };
    ticket: {
      adult_price: number;
      child_price: number;
      baby_price: number;
      ten_ve: string;
    }
  };
}

const FlightCard: FC<FlightCardProps> = ({
  className = "",
  data,
  defaultOpen = false,
}) => {
  const [isOpen, setIsOpen] = useState(defaultOpen);    

  const renderDetailTop = () => {
    // Convert departure and arrival times to Date objects
    const departureTime = new Date(`1970-01-01T${data.departure_date.split(" ")[1]}`);
    const arrivalTime = new Date(`1970-01-01T${data.arrival_date.split(" ")[1]}`);
  
    // Calculate the time difference in milliseconds
    const timeDifferenceInMilliseconds: number = arrivalTime.getTime() - departureTime.getTime();
  
    // Convert the time difference to hours and minutes
    const hours: number = Math.floor(timeDifferenceInMilliseconds / (1000 * 60 * 60));
    const minutes: number = Math.floor((timeDifferenceInMilliseconds % (1000 * 60 * 60)) / (1000 * 60));
    
    return (
      <div>
        <div className="flex flex-col md:flex-row">
          <div className="w-24 md:w-20 lg:w-24 flex-shrink-0 md:pt-7">
            <img src={data.airlines.logo} className="w-10" alt="" />
          </div>
          <div className="flex my-5 md:my-0">
            <div className="flex-shrink-0 flex flex-col items-center py-2">
              <span className="block w-6 h-6 rounded-full border border-neutral-400"></span>
              <span className="block flex-grow border-l border-neutral-400 border-dashed my-1"></span>
              <span className="block w-6 h-6 rounded-full border border-neutral-400"></span>
            </div>
            <div className="ml-4 space-y-10 text-sm">
              <div className="flex flex-col space-y-1">
                <span className="text-neutral-500 dark:text-neutral-400">
                  {data.departure_date.split(" ")[0]} · {data.departure_date.split(" ")[1]}
                </span>
                <span className="font-semibold">
                  {data.departure_from}
                </span>
              </div>
              <div className="flex flex-col space-y-1">
                <span className="text-neutral-500 dark:text-neutral-400">
                  {data.arrival_date.split(" ")[0]} · {data.arrival_date.split(" ")[1]}
                </span>
                <span className="font-semibold">
                  {data.arrival_to}
                </span>
              </div>
            </div>
          </div>
          <div className="border-l border-neutral-200 dark:border-neutral-700 md:mx-6 lg:mx-10"></div>
          <ul className="text-sm text-neutral-500 dark:text-neutral-400 space-y-1 md:space-y-2">
            <li>{`Thời gian bay: ${hours} giờ ${minutes} phút`}</li>
            <li>{data.ten_may_bay} · {data.airlines.name}</li>
          </ul>
        </div>
      </div>
    );
  };
  

  const renderDetail = () => {
    if (!isOpen) return null;
    return (
      <div className="p-4 md:p-8 border border-neutral-200 dark:border-neutral-700 rounded-2xl ">
        {renderDetailTop()}
      </div>
    );
  };
  const matchResult1 = data.departure_from.match(/\(([^)]+)\)/);
  const matchResult2 = data.arrival_to.match(/\(([^)]+)\)/);
  const departureTime = new Date(`1970-01-01T${data.departure_date.split(" ")[1]}`);
    const arrivalTime = new Date(`1970-01-01T${data.arrival_date.split(" ")[1]}`);
  
    // Calculate the time difference in milliseconds
    const timeDifferenceInMilliseconds: number = arrivalTime.getTime() - departureTime.getTime();
  
    // Convert the time difference to hours and minutes
    const hours: number = Math.floor(timeDifferenceInMilliseconds / (1000 * 60 * 60));
    const minutes: number = Math.floor((timeDifferenceInMilliseconds % (1000 * 60 * 60)) / (1000 * 60));
  return (
    <div
      className={`nc-FlightCardgroup p-4 sm:p-6 relative bg-white dark:bg-neutral-900 border border-neutral-100
     dark:border-neutral-800 rounded-2xl overflow-hidden hover:shadow-lg transition-shadow space-y-6 ${className}`}
      data-nc-id="FlightCard"
    >
      <div
        className={` sm:pr-20 relative  ${className}`}
        data-nc-id="FlightCard"
      >
        {/*  eslint-disable-next-line jsx-a11y/anchor-has-content */}
        <a href="##" className="absolute inset-0" />

        <span
          className={`absolute right-0 bottom-0 sm:bottom-auto sm:top-1/2 sm:-translate-y-1/2 w-10 h-10 bg-neutral-50 dark:bg-neutral-800 rounded-full flex items-center justify-center cursor-pointer ${
            isOpen ? "transform -rotate-180" : ""
          }`}
          onClick={() => setIsOpen(!isOpen)}
        >
          <i className="text-xl las la-angle-down"></i>
        </span>

        <div className="flex  flex-col sm:flex-row sm:items-center space-y-6 sm:space-y-0">
          {/* LOGO IMG */}
          <div className="w-24 lg:w-32 flex-shrink-0">
            <img src={data.airlines.logo} className="w-10" alt="" />
          </div>

          {/* TIME - NAME */}
          <div className="hidden lg:block  min-w-[150px] flex-[4] ">
            <div className="font-medium text-lg">{data.departure_date.split(" ")[1]} - {data.arrival_date.split(" ")[1]}</div>
            <div className="text-sm text-neutral-500 font-normal mt-0.5">
              {data.airlines.name}
            </div>
          </div>

          {/* TIMME */}
          <div className="hidden lg:block flex-[4] whitespace-nowrap">
            <div className="font-medium text-lg"> {matchResult1 ? matchResult1[1] : ''} - {matchResult2 ? matchResult2[1] : ''}</div>
            <div className="text-sm text-neutral-500 font-normal mt-0.5">
            {`${hours} giờ ${minutes} phút`}
            </div>
          </div>

          {/* TYPE */}
          <div className="hidden lg:block flex-[4] whitespace-nowrap">
            <div className="font-medium text-lg">Ngày bay</div>
            <div className="text-sm text-neutral-500 font-normal mt-0.5">
              {data.departure_date.split(' ')[0]}
            </div>
          </div>

          {/* PRICE */}
          <div className="flex-[4] whitespace-nowrap sm:text-right">
          </div>
        </div>
      </div>

      {/* DETAIL */}
      {renderDetail()}
    </div>
  );
};

export default FlightCard;

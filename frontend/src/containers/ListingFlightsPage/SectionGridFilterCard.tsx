import React, { FC } from "react";
import TabFilters from "./TabFilters";
import FlightCard, { FlightCardProps } from "components/FlightCard/FlightCard";

export interface SectionGridFilterCardProps {
  className?: string;
}

const DEMO_DATA: FlightCardProps["data"][] = [
  {
    id: "6b5515ab-b732-41f7-96a1-662da50a17ab",
    departure_date: "2024-01-08 17:00",
    arrival_date: '2024-01-08 19:00',
    departure_from: 'Hà Nội (HNA)',
    arrival_to: 'Hồ Chí Minh (SGN)',
    ten_may_bay: 'VN001',
    airlines: {
      logo: "https://seeklogo.com/images/V/Vietnam_Airlines-logo-6AB0B5A286-seeklogo.com.png",
      name: "Vietnam Airlines",
    },
    ticket: {
      adult_price: 123,
      child_price: 123,
      baby_price: 123,
      ten_ve: 'string'
    },
  },
  {
    id: "10d927a1-0a14-4c17-8226-4c7a3aad9e00",
    departure_date: "2024-01-09 17:00",
    arrival_date: '2024-01-09 19:00',
    departure_from: 'Hà Nội (HAN)',
    arrival_to: 'Hồ Chí Minh (SGN)',
    ten_may_bay: 'VN002',
    airlines: {
      logo: "https://seeklogo.com/images/V/Vietnam_Airlines-logo-6AB0B5A286-seeklogo.com.png",
      name: "Vietnam Airlines",
    },
    ticket: {
      adult_price: 123,
      child_price: 123,
      baby_price: 123,
      ten_ve: 'string'
    },
  },
  {
    id: "cc8dd6b2-a9fb-4c74-b167-135d2ee6eb07",
    departure_date: "2024-01-10 18:00",
    arrival_date: '2024-01-10 19:30',
    departure_from: 'Hà Nội (HAN)',
    arrival_to: 'Đà Nẵng (DAD)',
    ten_may_bay: 'VN003',
    airlines: {
      logo: "https://www.senviet.art/wp-content/uploads/edd/2017/08/Logo-VietjetAir.jpg",
      name: "Vietjet Air",
    },
    ticket: {
      adult_price: 123,
      child_price: 123,
      baby_price: 123,
      ten_ve: 'string'
    },
  },
  {
    id: "a23d6534-775c-4512-ab11-3bdd285a7ab5",
    departure_date: "2024-01-10 20:00",
    arrival_date: '2024-01-10 21:30',
    departure_from: 'Đà Nẵng (DAD)',
    arrival_to: 'Hà Nội (HAN)',
    ten_may_bay: 'VJ005',
    airlines: {
      logo: "https://www.senviet.art/wp-content/uploads/edd/2017/08/Logo-VietjetAir.jpg",
      name: "Vietjet Air",
    },
    ticket: {
      adult_price: 123,
      child_price: 123,
      baby_price: 123,
      ten_ve: 'string'
    },
  },
  {
    id: "e818c1c0-8755-4b92-a3e8-93796b3b1276",
    departure_date: "2024-01-10 20:00",
    arrival_date: '2024-01-10 21:30',
    departure_from: 'Đà Nẵng (DAD)',
    arrival_to: 'Hà Nội (HAN)',
    ten_may_bay: 'VN004',
    airlines: {
      logo: "https://seeklogo.com/images/V/Vietnam_Airlines-logo-6AB0B5A286-seeklogo.com.png",
      name: "Vietnam Airlines",
    },
    ticket: {
      adult_price: 123,
      child_price: 123,
      baby_price: 123,
      ten_ve: 'string'
    },
  },
  {
    id: "29354dc6-7c1b-4c77-b92e-3f1cfd8a261d",
    departure_date: "2024-01-12 20:00",
    arrival_date: '2024-01-12 21:30',
    departure_from: 'Huế (HUI)',
    arrival_to: 'Hà Nội (HNA)',
    ten_may_bay: 'QH008',
    airlines: {
      logo: "data:image/png;base64,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",
      name: "Bamboo Airways",
    },
    ticket: {
      adult_price: 123,
      child_price: 123,
      baby_price: 123,
      ten_ve: 'string'
    },
  },
  {
    id: "4f91932b-c673-4331-8fef-680564d54b74",
    departure_date: "2024-01-12 20:00",
    arrival_date: '2024-01-12 21:30',
    departure_from: 'Huế (HUI)',
    arrival_to: 'Hà Nội (HNA)',
    ten_may_bay: 'VJ007',
    airlines: {
      logo: "https://www.senviet.art/wp-content/uploads/edd/2017/08/Logo-VietjetAir.jpg",
      name: "Vietjet Air",
    },
    ticket: {
      adult_price: 123,
      child_price: 123,
      baby_price: 123,
      ten_ve: 'string'
    },
  },
  {
    id: "6f98b7b2-dcd2-4384-bff8-a941e640b84c",
    departure_date: "2024-01-12 20:00",
    arrival_date: '2024-01-12 21:30',
    departure_from: 'Hồ Chí Minh (SGN)',
    arrival_to: 'Đà Nẵng (DAD)',
    ten_may_bay: 'VJ005',
    airlines: {
      logo: "https://www.senviet.art/wp-content/uploads/edd/2017/08/Logo-VietjetAir.jpg",
      name: "Vietjet Air",
    },
    ticket: {
      adult_price: 123,
      child_price: 123,
      baby_price: 123,
      ten_ve: 'string'
    },
  },
  {
    id: "b6385182-2b52-447a-8c59-3711f52f897e",
    departure_date: "2024-01-12 20:00",
    arrival_date: '2024-01-12 21:30',
    departure_from: 'Huế (HUI)',
    arrival_to: 'Hồ Chí Minh (SGN)',
    ten_may_bay: 'VJ006',
    airlines: {
      logo: "https://www.senviet.art/wp-content/uploads/edd/2017/08/Logo-VietjetAir.jpg",
      name: "Vietjet Air",
    },
    ticket: {
      adult_price: 123,
      child_price: 123,
      baby_price: 123,
      ten_ve: 'string'
    },
  },
  {
    id: "abe0d2d2-425b-4e0b-9bc0-17cd62962167",
    departure_date: "2024-01-30 20:00",
    arrival_date: '2024-01-30 21:30',
    departure_from: 'Quy Nhơn (UIH)',
    arrival_to: 'Hà Nội (HNA)',
    ten_may_bay: 'QH009',
    airlines: {
      logo: "data:image/png;base64,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",
      name: "Bamboo Airways",
    },
    ticket: {
      adult_price: 123,
      child_price: 123,
      baby_price: 123,
      ten_ve: 'string'
    },
  },
  {
    id: "3434c8b4-c090-4320-bac7-be34dda80a03",
    departure_date: "2024-01-30 22:00",
    arrival_date: '2024-01-30 23:30',
    departure_from: 'Hà Nội (HNA)',
    arrival_to: 'Quy Nhơn (UIH)',
    ten_may_bay: 'QH010',
    airlines: {
      logo: "data:image/png;base64,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",
      name: "Bamboo Airways",
    },
    ticket: {
      adult_price: 123,
      child_price: 123,
      baby_price: 123,
      ten_ve: 'string'
    },
  },
];

const SectionGridFilterCard: FC<SectionGridFilterCardProps> = ({
  className = "",
}) => {
  return (
    <div
      className={`nc-SectionGridFilterCard ${className}`}
      data-nc-id="SectionGridFilterCard"
    >
      <div className="mb-8 lg:mb-11">
        <TabFilters />
      </div>
      <div className="lg:p-10 lg:bg-neutral-50 lg:dark:bg-black/20 grid grid-cols-1 gap-6  rounded-3xl">
        {DEMO_DATA.map((item, index) => (
          <FlightCard defaultOpen={!index} key={index} data={item} />
        ))}
      </div>
    </div>
  );
};

export default SectionGridFilterCard;

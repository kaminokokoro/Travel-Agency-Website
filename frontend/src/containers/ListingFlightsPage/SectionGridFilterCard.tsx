import React, { FC, useEffect, useState } from "react";
import TabFilters from "./TabFilters";
import Heading2 from "components/Heading/Heading2";
import FlightCard, { FlightCardProps } from "components/FlightCard/FlightCard";
import ButtonPrimary from "shared/Button/ButtonPrimary";
import { FlightProvider, Flight, FlightTicket} from 'data/types'
import { Server } from "../../Sever";



export interface SectionGridFilterCardProps {
  className?: string;
}

const DEMO_DATA: FlightCardProps["data"][] = [
  {
    id: "1",
    airlines: {
      logo: "https://www.gstatic.com/flights/airline_logos/70px/KE.png",
      name: "Korean Air",
    },
    ticket: {
      adult_price: 4100,
      id: 'dsa',
      name: "dsa",
      description: "sda",
      seat_class: "bus",
      child_price: 12,
      baby_price: 12,
      flight_id: 'ad'
    },
  },
  {
    id: "2",
    ticket: {
      adult_price: 4100,
      id: 'dsa',
      name: "dsa",
      description: "sda",
      seat_class: "bus",
      child_price: 12,
      baby_price: 12,
      flight_id: 'ad'
    },
    airlines: {
      logo: "https://www.gstatic.com/flights/airline_logos/70px/SQ.png",
      name: "Singapore Airlines",
    },
  },
  {
    id: "3",
    ticket: {
      adult_price: 4100,
      id: 'dsa',
      name: "dsa",
      description: "sda",
      seat_class: "bus",
      child_price: 12,
      baby_price: 12,
      flight_id: 'ad'
    },
    airlines: {
      logo: "https://www.gstatic.com/flights/airline_logos/70px/multi.png",
      name: "Philippine Airlines",
    },
  },
];

function useAllFlightProvider() {
  const [flightProviders, setFlightProviders] = useState<FlightProvider[] | undefined>(undefined);

  useEffect(() => {
    const fetchFlightProviders = async () => {
      try {
        const data = await new Server().getAllFlightProvider();
        setFlightProviders(data);
      } catch (error) {
        console.error("Error fetching flight providers:", error);
      }
    };

    fetchFlightProviders();
  }, []);

  return flightProviders;
}

function useAllFlights() {
  const [flights, setFlights] = useState<Flight[] | undefined>(undefined);

  useEffect(() => {
    const fetchFlights = async () => {
      try {
        const data = await new Server().getAllFlight();
        setFlights(data);
      } catch (error) {
        console.error("Error fetching flights:", error);
      }
    };

    fetchFlights();
  }, []);

  return flights;
}

function useFlightTicket(flight_id: string) {
  const [flightTicket, setFlightTicket] = useState<FlightTicket[] | undefined>(undefined);

  useEffect(() => {
    const fetchFlights = async () => {
      try {
        const data = await new Server().getFlightTicketByFlId(flight_id);
        setFlightTicket(data);
      } catch (error) {
        console.error("Error fetching flights:", error);
      }
    };

    fetchFlights();
  }, []);

  return flightTicket;
}

const SectionGridFilterCard: FC<SectionGridFilterCardProps> = ({
  className = "",
}) => {

  const flight_providers = useAllFlightProvider();
  const flights = useAllFlights();
  console.log(flight_providers);


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
          <FlightCard defaultOpen={index === 0} key={index} data={item} />
        ))}

        <div className="flex mt-12 justify-center items-center">
          <ButtonPrimary>Show more</ButtonPrimary>
        </div>
      </div>
    </div>
  );
};

export default SectionGridFilterCard;

//  ######  CustomLink  ######## //
export interface CustomLink {
  label: string;
  href: string;
  targetBlank?: boolean;
}

//  ##########  PostDataType ######## //
export interface TaxonomyType {
  id: string | number;
  name: string;
  href?: string;
  count?: number;
  thumbnail?: string;
  desc?: string;
  color?: TwMainColor | string;
  listingType?: "stay" | "experiences";
}


export type TwMainColor =
  | "pink"
  | "green"
  | "yellow"
  | "red"
  | "indigo"
  | "blue"
  | "purple"
  | "gray";

//


export interface Hotel {
  name: string;
  phone_number?: string;
  address: string;
  state?: string;
  id: string;
  description?: string;
  city?: string;
  zip_code?: number;
  average_rating: number;
  rating_count: number;
  min_price: number;
  galleryImgs: string[];
  href?: string;
}

export interface HotelService {
  id: string;
  name: string;
  room_type: string;
  room_capacity: number;
  description: string;
  price: number;
  hotel_id: string;
}

export interface HotelRatingByHotelId {
  id: string;
  rating: number;
  user_id: string;
  hotel_id: string;
  comments: string;
}

export interface UserProfile {
  last_name: string;
  first_name: string;
  email: string;
  city: string;
  zip_code: string;
  user_id: string;
  gender: boolean;
  id: string;
  street: string;
  state: string;
  date_of_birth: string;
}


//
export interface ExperiencesDataType {
  id: string | number;
  date: string;
  href: string;
  title: string;
  address: string;
  average_rating: number;
  rating_count: number;
  galleryImgs: string[];
  price: string;
}

export interface FlightProvider {
  id: string;
  name: string;
  description: string;
  email: string;
  phone_number: string;
}

export interface Flight {
  id: string;
  name: string;
  description: string;
  departure_from: string;
  arrival_to: string;
  departure_date: string;
  arrival_date: string;
  flight_provider_id: string;
}

export interface FlightTicket {
  id: string;
  name: string;
  description: string;
  seat_class: string;
  adult_price: number;
  child_price: number;
  baby_price: number;
  flight_id: string;
}

//
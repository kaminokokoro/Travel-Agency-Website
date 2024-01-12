
export interface CustomLink {
  label: string;
  href: string;
  targetBlank?: boolean;
}

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
export interface StayDataType {
  id: string | number;
  date: string;
  href: string;
  name: string;
  address: string;
  average_rating: number;
  rating_count: number;
  galleryImgs: string[];
  min_price: string;
}

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

//
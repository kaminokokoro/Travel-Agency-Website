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
  href: string;
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
  title: string;
  address: string;
  average_rating: number;
  rating_count: number;
  galleryImgs: string[];
  price: string;
}

export interface Hotel {
  name: string;
  phone_number: string;
  address: string;
  state: string;
  id: string;
  description: string;
  city: string;
  zip_code: number;
  average_rating: number;
  rating_count: number;
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


//
export interface ExperiencesDataType {
  id: string | number;
  date: string;
  href: string;
  title: string;
  // featuredImage: string;
  // commentCount: number;
  // viewCount: number;
  address: string;
  average_rating: number;
  rating_count: number;
  galleryImgs: string[];
  price: string;
  // listingCategory: TaxonomyType;
  // maxGuests: number;
}

//

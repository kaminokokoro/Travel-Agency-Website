import {Hotel, HotelRatingByHotelId} from 'data/types'

export interface HotelProps {
  hotel: Hotel[]
}

export interface HotelSingle {
  hotel: Hotel
}

export interface HotelRatingProps {
  "Hotel Rating": HotelRatingByHotelId[]
}

export class Server {
  
    baseUrl = "http://127.0.0.1:8000"

    async getAllHotel(page_number: number = 1, page_size: number = 10): Promise<HotelProps> {
      try {
        const response = await fetch(`${this.baseUrl}/hotel/all?page_number=${page_number}&page_size=${page_size}`);
        if (!response.ok) {
          throw new Error(`Request failed with status: ${response.status}`);
        }
        const data = await response.json();
        return data;
      } catch (error) {
        console.error("Error fetching places:", error);
        throw error;
      }
    }

    async getFilteredHotel(name_hotel: string = '', city_hotel: string = '', page_number: number = 1, page_size: number = 10): Promise<HotelProps> {
      try {
        const queryParams = new URLSearchParams({
          name_hotel: name_hotel,
          city_hotel: city_hotel,
          page_number: page_number.toString(),
          page_size: page_size.toString(),
        });
    
        const response = await fetch(`${this.baseUrl}/hotel/filter?${queryParams}`);
        if (!response.ok) {
          throw new Error(`Request failed with status: ${response.status}`);
        }
    
        const data = await response.json();
        return data;
      } catch (error) {
        console.error("Error fetching places:", error);
        throw error;
      }
    }

    async getHotel(id: string): Promise<HotelSingle> {
      try {
        const response = await fetch(`${this.baseUrl}/hotel/?hotel_id=${id}`);
        if (!response.ok) {
          throw new Error(`Request failed with status: ${response.status}`);
        }
        const data = await response.json();
        return data;
      } catch (error) {
        console.error("Error fetching places:", error);
        throw error;
      }
    }

    async getHotelRatingByHotelId(id: string, page_number: number = 1, page_size: number = 99999999): Promise<HotelRatingProps> {
      try {
        const response = await fetch(`${this.baseUrl}/hotel-rating/all/hotel?hotel_id=${id}&page_num=${page_number}&page_size=${page_size}`);
        if (!response.ok) {
          throw new Error(`Request failed with status: ${response.status}`);
        }
        const data = await response.json();
        return data;
      } catch (error) {
        console.error("Error fetching places:", error);
        throw error;
      }
    }
    
    
  
  }



import { tokens } from "../theme";

// Services

// Hotel
export const mockDataHotels = [
  {
    id: 1,
    hotelName: "Khach San A",
    address: "Ha Noi",
    phone: "(232)545-2345"
  },
  {
    id: 2,
    hotelName: "Khach San B",
    address: "Hai Phong",
    phone: "(232)545-7654"
  },
  {
    id: 3,
    hotelName: "Khach San C",
    address: "Bac Giang",
    phone: "(232)545-7233"
  },
  {
    id: 4,
    hotelName: "Khach San D",
    address: "Hai Duong",
    phone: "(232)545-6483"
  },
  {
    id: 5,
    hotelName: "Khach San E",
    address: "Thanh Hoa",
    phone: "(232)545-1234"
  },
  {
    id: 6,
    hotelName: "Khach San F",
    address: "Quang Ninh",
    phone: "(232)545-9876"
  },
  {
    id: 7,
    hotelName: "Khach San G",
    address: "Da Nang",
    phone: "(232)545-4567"
  },
  {
    id: 8,
    hotelName: "Khach San H",
    address: "Nha Trang",
    phone: "(232)545-8765"
  },
  {
    id: 9,
    hotelName: "Khach San I",
    address: "Can Tho",
    phone: "(232)545-3456"
  },
  {
    id: 10,
    hotelName: "Khach San K",
    address: "Vung Tau",
    phone: "(232)545-5678"
  },
  // Add more elements as needed
];


// Flight
export const mockDataFlights = [
  {
    id: 1,
    flightProvider: "Vietnam Airlines",
    flightCode: "ABC123",
    flightOrigin: "CityA",
    flightDestination: "CityB",
    duration: "3 hours"
  },
  {
    id: 2,
    flightProvider: "Delta Airlines",
    flightCode: "DEF456",
    flightOrigin: "CityC",
    flightDestination: "CityD",
    duration: "4 hours"
  },
  {
    id: 3,
    flightProvider: "Emirates",
    flightCode: "GHI789",
    flightOrigin: "CityE",
    flightDestination: "CityF",
    duration: "6 hours"
  },
  {
    id: 4,
    flightProvider: "United Airlines",
    flightCode: "JKL012",
    flightOrigin: "CityG",
    flightDestination: "CityH",
    duration: "2.5 hours"
  },
  {
    id: 5,
    flightProvider: "Qatar Airways",
    flightCode: "MNO345",
    flightOrigin: "CityI",
    flightDestination: "CityJ",
    duration: "5 hours"
  },
  {
    id: 6,
    flightProvider: "Singapore Airlines",
    flightCode: "PQR678",
    flightOrigin: "CityK",
    flightDestination: "CityL",
    duration: "7 hours"
  },
  {
    id: 7,
    flightProvider: "Air France",
    flightCode: "STU901",
    flightOrigin: "CityM",
    flightDestination: "CityN",
    duration: "4.5 hours"
  },
  {
    id: 8,
    flightProvider: "Lufthansa",
    flightCode: "VWX234",
    flightOrigin: "CityO",
    flightDestination: "CityP",
    duration: "6.5 hours"
  },
  {
    id: 9,
    flightProvider: "American Airlines",
    flightCode: "YZA567",
    flightOrigin: "CityQ",
    flightDestination: "CityR",
    duration: "3.5 hours"
  },
  {
    id: 10,
    flightProvider: "Cathay Pacific",
    flightCode: "BCD890",
    flightOrigin: "CityS",
    flightDestination: "CityT",
    duration: "8 hours"
  },
  // Add more elements as needed
];

// Tour
export const mockDataTours = [
  {
    id: 1,
    tourName: "Tropical Retreat",
    tourDestination: "Rocky Mountains, USA",
    duration: "3 hours"
  },
  {
    id: 2,
    tourName: "Mountain Adventure",
    tourDestination: "Swiss Alps",
    duration: "5 hours"
  },
  {
    id: 3,
    tourName: "Desert Expedition",
    tourDestination: "Sahara Desert, Morocco",
    duration: "2 days"
  },
  {
    id: 4,
    tourName: "Island Paradise",
    tourDestination: "Bora Bora, French Polynesia",
    duration: "7 days"
  },
  {
    id: 5,
    tourName: "City Escape",
    tourDestination: "New York City, USA",
    duration: "2 days"
  },
  {
    id: 6,
    tourName: "Jungle Safari",
    tourDestination: "Amazon Rainforest, Brazil",
    duration: "4 days"
  },
  {
    id: 7,
    tourName: "Historical Journey",
    tourDestination: "Rome, Italy",
    duration: "3 days"
  },
  {
    id: 8,
    tourName: "Winter Wonderland",
    tourDestination: "Banff National Park, Canada",
    duration: "4 days"
  },
  {
    id: 9,
    tourName: "Beach Getaway",
    tourDestination: "Phuket, Thailand",
    duration: "5 days"
  },
  {
    id: 10,
    tourName: "Cultural Experience",
    tourDestination: "Kyoto, Japan",
    duration: "3 days"
  },
  // Add more elements as needed
];

// Booking

// Hotel
export const mockDataBookingHotels = [
  {
    id: 1,
    hotelName: "Khach San A",
    hotelServiceId: 101,
    userBooked: "tuannguyen213@gmail.com",
    checkIn: "04-01-2023",
    checkOut: "10-01-2023",
    paymentTime: "03-01-2023 15:30:00"
  },
  {
    id: 2,
    hotelName: "Khach San E",
    hotelServiceId: 101,
    userBooked: "0823910371",
    checkIn: "23-04-2023",
    checkOut: "30-04-2023",
    paymentTime: "20-04-2023 18:32:41"
  },
  {
    id: 3,
    hotelName: "Khach San B",
    hotelServiceId: 102,
    userBooked: "john.doe@example.com",
    checkIn: "15-05-2023",
    checkOut: "20-05-2023",
    paymentTime: "10-05-2023 10:15:00"
  },
  {
    id: 4,
    hotelName: "Khach San C",
    hotelServiceId: 103,
    userBooked: "alice.smith@example.com",
    checkIn: "01-07-2023",
    checkOut: "05-07-2023",
    paymentTime: "25-06-2023 14:45:30"
  },
  {
    id: 5,
    hotelName: "Khach San D",
    hotelServiceId: 104,
    userBooked: "0987654321",
    checkIn: "12-08-2023",
    checkOut: "18-08-2023",
    paymentTime: "08-08-2023 09:20:15"
  },
  {
    id: 6,
    hotelName: "Khach San F",
    hotelServiceId: 105,
    userBooked: "jane.doe@example.com",
    checkIn: "09-09-2023",
    checkOut: "15-09-2023",
    paymentTime: "05-09-2023 17:12:00"
  },
  {
    id: 7,
    hotelName: "Khach San G",
    hotelServiceId: 106,
    userBooked: "0912345678",
    checkIn: "02-11-2023",
    checkOut: "08-11-2023",
    paymentTime: "28-10-2023 20:00:45"
  },
  {
    id: 8,
    hotelName: "Khach San H",
    hotelServiceId: 107,
    userBooked: "bob.smith@example.com",
    checkIn: "14-12-2023",
    checkOut: "20-12-2023",
    paymentTime: "10-12-2023 12:30:20"
  },
  {
    id: 9,
    hotelName: "Khach San I",
    hotelServiceId: 108,
    userBooked: "0765432109",
    checkIn: "17-01-2024",
    checkOut: "23-01-2024",
    paymentTime: "12-01-2024 09:45:10"
  },
  {
    id: 10,
    hotelName: "Khach San J",
    hotelServiceId: 109,
    userBooked: "emily.jones@example.com",
    checkIn: "05-02-2024",
    checkOut: "11-02-2024",
    paymentTime: "01-02-2024 14:10:30"
  }
];

// Flight
export const mockDataBookingFlights = [
  {
    id: 1,
    flightProvider: "Vietnam Airlines",
    departureDate: "15-01-2024",
    returnDate: null,
    userBooked: "tuannguyen213@gmail.com",
    paymentTime: "10-12-2023 12:30:20"
  },
  {
    id: 2,
    flightProvider: "Air France",
    departureDate: "25-12-2023",
    returnDate: "08-01-2024",
    userBooked: "0512798561",
    paymentTime: "24-12-2023 14:32:11"
  },
  {
    id: 3,
    flightProvider: "Lufthansa",
    departureDate: "18-02-2024",
    returnDate: "25-02-2024",
    userBooked: "john.doe@example.com",
    paymentTime: "15-01-2024 09:45:55"
  },
  {
    id: 4,
    flightProvider: "Emirates",
    departureDate: "02-03-2024",
    returnDate: null,
    userBooked: "mary.smith@example.com",
    paymentTime: "28-02-2024 16:18:42"
  },
  {
    id: 5,
    flightProvider: "Delta Airlines",
    departureDate: "10-04-2024",
    returnDate: "18-04-2024",
    userBooked: "1234567890",
    paymentTime: "05-04-2024 11:20:30"
  },
  {
    id: 6,
    flightProvider: "Qatar Airways",
    departureDate: "22-05-2024",
    returnDate: "30-05-2024",
    userBooked: "jane.doe@example.com",
    paymentTime: "18-05-2024 08:37:15"
  },
  {
    id: 7,
    flightProvider: "Singapore Airlines",
    departureDate: "15-06-2024",
    returnDate: null,
    userBooked: "9876543210",
    paymentTime: "10-06-2024 15:12:40"
  },
  {
    id: 8,
    flightProvider: "American Airlines",
    departureDate: "05-07-2024",
    returnDate: "12-07-2024",
    userBooked: "alice.johnson@example.com",
    paymentTime: "30-06-2024 10:05:22"
  },
  {
    id: 9,
    flightProvider: "British Airways",
    departureDate: "18-08-2024",
    returnDate: "25-08-2024",
    userBooked: "0987654321",
    paymentTime: "12-08-2024 13:28:18"
  },
  {
    id: 10,
    flightProvider: "Turkish Airlines",
    departureDate: "01-09-2024",
    returnDate: null,
    userBooked: "peter.wong@example.com",
    paymentTime: "25-08-2024 19:50:07"
  }
];

// Tour
export const mockDataBookingTours = [
  {
    id: 1,
    tourName: "Tropical Retreat",
    departureDate: "15-01-2024",
    returnDate: null,
    userBooked: "tuannguyen213@gmail.com",
    paymentTime: "10-12-2023 12:30:20"
  },
  {
    id: 2,
    tourName: "Mountain Adventure",
    departureDate: "20-02-2024",
    returnDate: "28-02-2024",
    userBooked: "alice.smith@example.com",
    paymentTime: "15-01-2024 09:45:10"
  },
  {
    id: 3,
    tourName: "City Explorer",
    departureDate: "10-03-2024",
    returnDate: "15-03-2024",
    userBooked: "john.doe@example.com",
    paymentTime: "25-02-2024 18:20:35"
  },
  {
    id: 4,
    tourName: "Beach Paradise",
    departureDate: "05-04-2024",
    returnDate: "12-04-2024",
    userBooked: "emma.jones@example.com",
    paymentTime: "02-03-2024 15:10:50"
  },
  {
    id: 5,
    tourName: "Historical Journey",
    departureDate: "18-05-2024",
    returnDate: "25-05-2024",
    userBooked: "michael.wilson@example.com",
    paymentTime: "12-04-2024 08:55:15"
  },
  {
    id: 6,
    tourName: "Wildlife Safari",
    departureDate: "10-06-2024",
    returnDate: "18-06-2024",
    userBooked: "sophia.anderson@example.com",
    paymentTime: "20-05-2024 14:30:40"
  },
  {
    id: 7,
    tourName: "Cultural Immersion",
    departureDate: "15-07-2024",
    returnDate: "22-07-2024",
    userBooked: "william.taylor@example.com",
    paymentTime: "01-06-2024 11:25:05"
  },
  {
    id: 8,
    tourName: "Island Getaway",
    departureDate: "08-08-2024",
    returnDate: "15-08-2024",
    userBooked: "olivia.jackson@example.com",
    paymentTime: "10-07-2024 17:45:30"
  },
  {
    id: 9,
    tourName: "Mystical Adventure",
    departureDate: "20-09-2024",
    returnDate: "28-09-2024",
    userBooked: "noah.thompson@example.com",
    paymentTime: "15-08-2024 09:20:55"
  },
  {
    id: 10,
    tourName: "Desert Expedition",
    departureDate: "12-10-2024",
    returnDate: "20-10-2024",
    userBooked: "ava.miller@example.com",
    paymentTime: "25-09-2024 22:15:20"
  }
];

//User
export const mockUserData = [
  {
    id: 1,
    name: "Nguyen Van A",
    phoneNumber: "0831991023",
    mail: "ngvanA@gmail.com",
    authorize: 1
  },
  {
    id: 2,
    name: "Tran Thi B",
    phoneNumber: "0908765432",
    mail: "tranB@example.com",
    authorize: 2
  },
  {
    id: 3,
    name: "Le Van C",
    phoneNumber: "0987654321",
    mail: "levanC@example.com",
    authorize: 3
  },
  {
    id: 4,
    name: "Pham Thi D",
    phoneNumber: "0854321098",
    mail: "phamD@example.com",
    authorize: 1
  },
  {
    id: 5,
    name: "Hoang Van E",
    phoneNumber: "0932108765",
    mail: "hoangE@gmail.com",
    authorize: 2
  },
  {
    id: 6,
    name: "Do Thi F",
    phoneNumber: "0876543210",
    mail: "doF@example.com",
    authorize: 3
  },
  {
    id: 7,
    name: "Truong Van G",
    phoneNumber: "0812345678",
    mail: "truongG@gmail.com",
    authorize: 1
  },
  {
    id: 8,
    name: "Nguyen Thi H",
    phoneNumber: "0945678901",
    mail: "nguyenH@example.com",
    authorize: 2
  },
  {
    id: 9,
    name: "Vu Van I",
    phoneNumber: "0890123456",
    mail: "vuI@gmail.com",
    authorize: 3
  },
  {
    id: 10,
    name: "Le Thi K",
    phoneNumber: "0865432109",
    mail: "leK@example.com",
    authorize: 1
  }
];


// export const mockBarHotelData = [
//   { hotel: "Khach san A", rating: "1.3", "ratingColor": "hsl(176, 70%, 50%)" },
//   { hotel: "Khach san C", rating: "3.2", "ratingColor": "hsl(176, 70%, 50%)" },
//   { hotel: "Khach san E", rating: "4.5", "ratingColor": "hsl(176, 70%, 50%)" },
//   { hotel: "Khach san B", rating: "2.7", "ratingColor": "hsl(176, 70%, 50%)" },
//   { hotel: "Khach san J", rating: "4.1", "ratingColor": "hsl(176, 70%, 50%)" },
//   { hotel: "Khach san F", rating: "0.9", "ratingColor": "hsl(176, 70%, 50%)" },
//   { hotel: "Khach san M", rating: "3.8", "ratingColor": "hsl(176, 70%, 50%)" },
//   { hotel: "Khach san D", rating: "2.2", "ratingColor": "hsl(176, 70%, 50%)" },
//   { hotel: "Khach san L", rating: "4.9", "ratingColor": "hsl(176, 70%, 50%)" },
//   { hotel: "Khach san O", rating: "1.6", "ratingColor": "hsl(176, 70%, 50%)" },
// ];

// export const mockBarFlightData = [
//   { flightProvider: "Emirates", rating: "2.3", ratingColor: "hsl(204, 70%, 50%)" },
//   { flightProvider: "Delta Airlines", rating: "4.2", ratingColor: "hsl(204, 70%, 50%)" },
//   { flightProvider: "British Airways", rating: "3.5", ratingColor: "hsl(204, 70%, 50%)" },
//   { flightProvider: "Lufthansa", rating: "1.8", ratingColor: "hsl(204, 70%, 50%)" },
//   { flightProvider: "Qatar Airways", rating: "4.9", ratingColor: "hsl(204, 70%, 50%)" },
//   { flightProvider: "United Airlines", rating: "0.7", ratingColor: "hsl(204, 70%, 50%)" },
//   { flightProvider: "Singapore Airlines", rating: "3.2", ratingColor: "hsl(204, 70%, 50%)" },
//   { flightProvider: "Air France", rating: "2.6", ratingColor: "hsl(204, 70%, 50%)" },
//   { flightProvider: "Cathay Pacific", rating: "4.0", ratingColor: "hsl(204, 70%, 50%)" },
//   { flightProvider: "American Airlines", rating: "1.4", ratingColor: "hsl(204, 70%, 50%)" },
// ];

// export const mockBarTourData = [
//   { tour: "Tropical Retreat", rating: "4.9" },
//   { tour: "Mountain Adventure", rating: "4.8" },
//   { tour: "City Explorer", rating: "4.7" },
//   { tour: "Island Paradise", rating: "4.6" },
//   { tour: "Historical Journey", rating: "4.5" },
//   { tour: "Wildlife Safari", rating: "4.4" },
//   { tour: "Desert Expedition", rating: "4.3" },
//   { tour: "Northern Lights Discovery", rating: "4.2" },
//   { tour: "Cruise Along the Riviera", rating: "4.1" },
//   { tour: "Mystical Forest Retreat", rating: "4.0" },
// ];




export const mockPieData = [
  {
    id: "hack",
    label: "hack",
    value: 239,
    color: "hsl(104, 70%, 50%)",
  },
  {
    id: "make",
    label: "make",
    value: 170,
    color: "hsl(162, 70%, 50%)",
  },
  {
    id: "go",
    label: "go",
    value: 322,
    color: "hsl(291, 70%, 50%)",
  },
  {
    id: "lisp",
    label: "lisp",
    value: 503,
    color: "hsl(229, 70%, 50%)",
  },
  {
    id: "scala",
    label: "scala",
    value: 584,
    color: "hsl(344, 70%, 50%)",
  },
];

export const mockLineData = [
  {
    id: "japan",
    color: tokens("dark").greenAccent[500],
    data: [
      {
        x: "plane",
        y: 101,
      },
      {
        x: "helicopter",
        y: 75,
      },
      {
        x: "boat",
        y: 36,
      },
      {
        x: "train",
        y: 216,
      },
      {
        x: "subway",
        y: 35,
      },
      {
        x: "bus",
        y: 236,
      },
      {
        x: "car",
        y: 88,
      },
      {
        x: "moto",
        y: 232,
      },
      {
        x: "bicycle",
        y: 281,
      },
      {
        x: "horse",
        y: 1,
      },
      {
        x: "skateboard",
        y: 35,
      },
      {
        x: "others",
        y: 14,
      },
    ],
  },
  {
    id: "france",
    color: tokens("dark").blueAccent[300],
    data: [
      {
        x: "plane",
        y: 212,
      },
      {
        x: "helicopter",
        y: 190,
      },
      {
        x: "boat",
        y: 270,
      },
      {
        x: "train",
        y: 9,
      },
      {
        x: "subway",
        y: 75,
      },
      {
        x: "bus",
        y: 175,
      },
      {
        x: "car",
        y: 33,
      },
      {
        x: "moto",
        y: 189,
      },
      {
        x: "bicycle",
        y: 97,
      },
      {
        x: "horse",
        y: 87,
      },
      {
        x: "skateboard",
        y: 299,
      },
      {
        x: "others",
        y: 251,
      },
    ],
  },
  {
    id: "us",
    color: tokens("dark").redAccent[200],
    data: [
      {
        x: "plane",
        y: 191,
      },
      {
        x: "helicopter",
        y: 136,
      },
      {
        x: "boat",
        y: 91,
      },
      {
        x: "train",
        y: 190,
      },
      {
        x: "subway",
        y: 211,
      },
      {
        x: "bus",
        y: 152,
      },
      {
        x: "car",
        y: 189,
      },
      {
        x: "moto",
        y: 152,
      },
      {
        x: "bicycle",
        y: 8,
      },
      {
        x: "horse",
        y: 197,
      },
      {
        x: "skateboard",
        y: 107,
      },
      {
        x: "others",
        y: 170,
      },
    ],
  },
];

export const mockGeographyData = [
  {
    id: "AFG",
    value: 520600,
  },
  {
    id: "AGO",
    value: 949905,
  },
  {
    id: "ALB",
    value: 329910,
  },
  {
    id: "ARE",
    value: 675484,
  },
  {
    id: "ARG",
    value: 432239,
  },
  {
    id: "ARM",
    value: 288305,
  },
  {
    id: "ATA",
    value: 415648,
  },
  {
    id: "ATF",
    value: 665159,
  },
  {
    id: "AUT",
    value: 798526,
  },
  {
    id: "AZE",
    value: 481678,
  },
  {
    id: "BDI",
    value: 496457,
  },
  {
    id: "BEL",
    value: 252276,
  },
  {
    id: "BEN",
    value: 440315,
  },
  {
    id: "BFA",
    value: 343752,
  },
  {
    id: "BGD",
    value: 920203,
  },
  {
    id: "BGR",
    value: 261196,
  },
  {
    id: "BHS",
    value: 421551,
  },
  {
    id: "BIH",
    value: 974745,
  },
  {
    id: "BLR",
    value: 349288,
  },
  {
    id: "BLZ",
    value: 305983,
  },
  {
    id: "BOL",
    value: 430840,
  },
  {
    id: "BRN",
    value: 345666,
  },
  {
    id: "BTN",
    value: 649678,
  },
  {
    id: "BWA",
    value: 319392,
  },
  {
    id: "CAF",
    value: 722549,
  },
  {
    id: "CAN",
    value: 332843,
  },
  {
    id: "CHE",
    value: 122159,
  },
  {
    id: "CHL",
    value: 811736,
  },
  {
    id: "CHN",
    value: 593604,
  },
  {
    id: "CIV",
    value: 143219,
  },
  {
    id: "CMR",
    value: 630627,
  },
  {
    id: "COG",
    value: 498556,
  },
  {
    id: "COL",
    value: 660527,
  },
  {
    id: "CRI",
    value: 60262,
  },
  {
    id: "CUB",
    value: 177870,
  },
  {
    id: "-99",
    value: 463208,
  },
  {
    id: "CYP",
    value: 945909,
  },
  {
    id: "CZE",
    value: 500109,
  },
  {
    id: "DEU",
    value: 63345,
  },
  {
    id: "DJI",
    value: 634523,
  },
  {
    id: "DNK",
    value: 731068,
  },
  {
    id: "DOM",
    value: 262538,
  },
  {
    id: "DZA",
    value: 760695,
  },
  {
    id: "ECU",
    value: 301263,
  },
  {
    id: "EGY",
    value: 148475,
  },
  {
    id: "ERI",
    value: 939504,
  },
  {
    id: "ESP",
    value: 706050,
  },
  {
    id: "EST",
    value: 977015,
  },
  {
    id: "ETH",
    value: 461734,
  },
  {
    id: "FIN",
    value: 22800,
  },
  {
    id: "FJI",
    value: 18985,
  },
  {
    id: "FLK",
    value: 64986,
  },
  {
    id: "FRA",
    value: 447457,
  },
  {
    id: "GAB",
    value: 669675,
  },
  {
    id: "GBR",
    value: 757120,
  },
  {
    id: "GEO",
    value: 158702,
  },
  {
    id: "GHA",
    value: 893180,
  },
  {
    id: "GIN",
    value: 877288,
  },
  {
    id: "GMB",
    value: 724530,
  },
  {
    id: "GNB",
    value: 387753,
  },
  {
    id: "GNQ",
    value: 706118,
  },
  {
    id: "GRC",
    value: 377796,
  },
  {
    id: "GTM",
    value: 66890,
  },
  {
    id: "GUY",
    value: 719300,
  },
  {
    id: "HND",
    value: 739590,
  },
  {
    id: "HRV",
    value: 929467,
  },
  {
    id: "HTI",
    value: 538961,
  },
  {
    id: "HUN",
    value: 146095,
  },
  {
    id: "IDN",
    value: 490681,
  },
  {
    id: "IND",
    value: 549818,
  },
  {
    id: "IRL",
    value: 630163,
  },
  {
    id: "IRN",
    value: 596921,
  },
  {
    id: "IRQ",
    value: 767023,
  },
  {
    id: "ISL",
    value: 478682,
  },
  {
    id: "ISR",
    value: 963688,
  },
  {
    id: "ITA",
    value: 393089,
  },
  {
    id: "JAM",
    value: 83173,
  },
  {
    id: "JOR",
    value: 52005,
  },
  {
    id: "JPN",
    value: 199174,
  },
  {
    id: "KAZ",
    value: 181424,
  },
  {
    id: "KEN",
    value: 60946,
  },
  {
    id: "KGZ",
    value: 432478,
  },
  {
    id: "KHM",
    value: 254461,
  },
  {
    id: "OSA",
    value: 942447,
  },
  {
    id: "KWT",
    value: 414413,
  },
  {
    id: "LAO",
    value: 448339,
  },
  {
    id: "LBN",
    value: 620090,
  },
  {
    id: "LBR",
    value: 435950,
  },
  {
    id: "LBY",
    value: 75091,
  },
  {
    id: "LKA",
    value: 595124,
  },
  {
    id: "LSO",
    value: 483524,
  },
  {
    id: "LTU",
    value: 867357,
  },
  {
    id: "LUX",
    value: 689172,
  },
  {
    id: "LVA",
    value: 742980,
  },
  {
    id: "MAR",
    value: 236538,
  },
  {
    id: "MDA",
    value: 926836,
  },
  {
    id: "MDG",
    value: 840840,
  },
  {
    id: "MEX",
    value: 353910,
  },
  {
    id: "MKD",
    value: 505842,
  },
  {
    id: "MLI",
    value: 286082,
  },
  {
    id: "MMR",
    value: 915544,
  },
  {
    id: "MNE",
    value: 609500,
  },
  {
    id: "MNG",
    value: 410428,
  },
  {
    id: "MOZ",
    value: 32868,
  },
  {
    id: "MRT",
    value: 375671,
  },
  {
    id: "MWI",
    value: 591935,
  },
  {
    id: "MYS",
    value: 991644,
  },
  {
    id: "NAM",
    value: 701897,
  },
  {
    id: "NCL",
    value: 144098,
  },
  {
    id: "NER",
    value: 312944,
  },
  {
    id: "NGA",
    value: 862877,
  },
  {
    id: "NIC",
    value: 90831,
  },
  {
    id: "NLD",
    value: 281879,
  },
  {
    id: "NOR",
    value: 224537,
  },
  {
    id: "NPL",
    value: 322331,
  },
  {
    id: "NZL",
    value: 86615,
  },
  {
    id: "OMN",
    value: 707881,
  },
  {
    id: "PAK",
    value: 158577,
  },
  {
    id: "PAN",
    value: 738579,
  },
  {
    id: "PER",
    value: 248751,
  },
  {
    id: "PHL",
    value: 557292,
  },
  {
    id: "PNG",
    value: 516874,
  },
  {
    id: "POL",
    value: 682137,
  },
  {
    id: "PRI",
    value: 957399,
  },
  {
    id: "PRT",
    value: 846430,
  },
  {
    id: "PRY",
    value: 720555,
  },
  {
    id: "QAT",
    value: 478726,
  },
  {
    id: "ROU",
    value: 259318,
  },
  {
    id: "RUS",
    value: 268735,
  },
  {
    id: "RWA",
    value: 136781,
  },
  {
    id: "ESH",
    value: 151957,
  },
  {
    id: "SAU",
    value: 111821,
  },
  {
    id: "SDN",
    value: 927112,
  },
  {
    id: "SDS",
    value: 966473,
  },
  {
    id: "SEN",
    value: 158085,
  },
  {
    id: "SLB",
    value: 178389,
  },
  {
    id: "SLE",
    value: 528433,
  },
  {
    id: "SLV",
    value: 353467,
  },
  {
    id: "ABV",
    value: 251,
  },
  {
    id: "SOM",
    value: 445243,
  },
  {
    id: "SRB",
    value: 202402,
  },
  {
    id: "SUR",
    value: 972121,
  },
  {
    id: "SVK",
    value: 319923,
  },
  {
    id: "SVN",
    value: 728766,
  },
  {
    id: "SWZ",
    value: 379669,
  },
  {
    id: "SYR",
    value: 16221,
  },
  {
    id: "TCD",
    value: 101273,
  },
  {
    id: "TGO",
    value: 498411,
  },
  {
    id: "THA",
    value: 506906,
  },
  {
    id: "TJK",
    value: 613093,
  },
  {
    id: "TKM",
    value: 327016,
  },
  {
    id: "TLS",
    value: 607972,
  },
  {
    id: "TTO",
    value: 936365,
  },
  {
    id: "TUN",
    value: 898416,
  },
  {
    id: "TUR",
    value: 237783,
  },
  {
    id: "TWN",
    value: 878213,
  },
  {
    id: "TZA",
    value: 442174,
  },
  {
    id: "UGA",
    value: 720710,
  },
  {
    id: "UKR",
    value: 74172,
  },
  {
    id: "URY",
    value: 753177,
  },
  {
    id: "USA",
    value: 658725,
  },
  {
    id: "UZB",
    value: 550313,
  },
  {
    id: "VEN",
    value: 707492,
  },
  {
    id: "VNM",
    value: 538907,
  },
  {
    id: "VUT",
    value: 650646,
  },
  {
    id: "PSE",
    value: 476078,
  },
  {
    id: "YEM",
    value: 957751,
  },
  {
    id: "ZAF",
    value: 836949,
  },
  {
    id: "ZMB",
    value: 714503,
  },
  {
    id: "ZWE",
    value: 405217,
  },
  {
    id: "KOR",
    value: 171135,
  },
];

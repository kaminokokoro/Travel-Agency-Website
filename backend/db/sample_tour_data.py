import random
from datetime import datetime, timedelta

from backend.crud.CRUDTour import crud_tour
from backend.crud.CRUDTourBooking import crud_tour_booking
from backend.crud.CRUDTourDate import crud_tour_date

from backend.util import schemas

# tour_name = [
#     "Serenity Shores Expedition",
#     "Cultural Mosaic Quest",
#     "Wilderness Adventure Trek",
#     "Enchanting Heritage Trail",
#     "Island Paradise Discovery",
#     "Epic Landscapes Escapade",
#     "Mystic Mountain Voyage",
#     "Coastal Bliss Retreat",
#     "Urban Wonders Wanderlust",
#     "Tranquil Oasis Odyssey",
#     "Sunset Serenade Sojourn",
#     "Northern Lights Expedition",
#     "Ancient Ruins Adventure",
#     "Jungle Safari Quest",
#     "Spiritual Sanctuary Sojourn",
#     "Whale Watching Wonders",
#     "Desert Mirage Trek",
#     "Hidden Gems Excursion",
#     "Festive Fiesta Discovery",
#     "Lakeside Retreat Expedition",
#     "Gastronomic Delights Discovery",
#     "Volcano Exploration Expedition",
#     "Historical Marvels Trail",
#     "Adventure at the Ends of the Earth",
#     "Tropical Rainforest Trek",
#     "Wellness Retreat Escape",
#     "Glacier Wonderland Adventure",
#     "Vibrant Cityscape Quest",
#     "Artisanal Crafts Expedition",
#     "Whispering Winds Retreat"
# ]
tours = [
    {
        "tour_name": "Tour 4 đảo Nam Phú Quốc - 1 ngày",
        "destination": "143 Trần Hưng Đạo, KP 7, TT Dương Đông, H.Phú Quốc, tỉnh Kiên Giang, Vietnam",
        "duration": "1",
        "description": "",
        "adult_price": 800000,
        "child_price": 400000
    },
    {
        "tour_name": "Cultural Mosaic Quest",
        "destination": "Historic Cities and Temples",
        "duration": "7 days / 6 nights",
        "description": "Immerse yourself in the diverse cultural heritage of ancient civilizations.",
        "adult_price": 700,
        "child_price": 350
    },
    {
        "tour_name": "Wilderness Adventure Trek",
        "destination": "Remote Mountain Ranges",
        "duration": "6 days / 5 nights",
        "description": "Embark on an adrenaline-pumping trek through untamed wilderness.",
        "adult_price": 600,
        "child_price": 300
    },
    # Bạn có thể thêm thông tin cho các tour du lịch khác ở đây
    {
        "tour_name": "Vibrant Cityscape Quest",
        "destination": "Metropolitan Adventure",
        "duration": "4 days / 3 nights",
        "description": "Explore the lively streets and cultural richness of a vibrant city.",
        "adult_price": 450,
        "child_price": 225
    },
    {
        "tour_name": "Artisanal Crafts Expedition",
        "destination": "Traditional Artisan Villages",
        "duration": "3 days / 2 nights",
        "description": "Discover the intricate craftsmanship and cultural heritage of artisanal villages.",
        "adult_price": 300,
        "child_price": 150
    },
    {
        "tour_name": "Whispering Winds Retreat",
        "destination": "Tranquil Countryside",
        "duration": "4 days / 3 nights",
        "description": "Rejuvenate in the peaceful ambiance of the countryside amid gentle winds.",
        "adult_price": 400,
        "child_price": 200
    }
    # Thêm thông tin cho các tour du lịch còn lại
]
# tours += [
#     {
#         "tour_name": "Sunset Serenade Sojourn",
#         "destination": "Coastal Retreat",
#         "duration": "3 days / 2 nights",
#         "description": "Witness mesmerizing sunsets on a serene coastal retreat.",
#         "adult_price": 350,
#         "child_price": 175
#     },
#     {
#         "tour_name": "Northern Lights Expedition",
#         "destination": "Arctic Wilderness",
#         "duration": "8 days / 7 nights",
#         "description": "Chase the ethereal beauty of the Northern Lights in the Arctic wilderness.",
#         "adult_price": 800,
#         "child_price": 400
#     },
#     {
#         "tour_name": "Ancient Ruins Adventure",
#         "destination": "Archaeological Sites",
#         "duration": "6 days / 5 nights",
#         "description": "Explore ancient ruins and uncover lost civilizations.",
#         "adult_price": 600,
#         "child_price": 300
#     },
#     {
#         "tour_name": "Jungle Safari Quest",
#         "destination": "Tropical Rainforests",
#         "duration": "5 days / 4 nights",
#         "description": "Embark on a thrilling safari adventure in lush tropical rainforests.",
#         "adult_price": 550,
#         "child_price": 275
#     },
#     {
#         "tour_name": "Spiritual Sanctuary Sojourn",
#         "destination": "Sacred Temples and Monasteries",
#         "duration": "7 days / 6 nights",
#         "description": "Find solace and spirituality in serene temples and monastic retreats.",
#         "adult_price": 700,
#         "child_price": 350
#     },
#     {
#         "tour_name": "Whale Watching Wonders",
#         "destination": "Coastal Waters",
#         "duration": "2 days / 1 night",
#         "description": "Witness the majestic beauty of whales in their natural habitat.",
#         "adult_price": 250,
#         "child_price": 125
#     },
#     {
#         "tour_name": "Desert Mirage Trek",
#         "destination": "Sandy Dunes",
#         "duration": "4 days / 3 nights",
#         "description": "Explore the mystical allure of the desert's sandy dunes.",
#         "adult_price": 450,
#         "child_price": 225
#     },
#     {
#         "tour_name": "Hidden Gems Excursion",
#         "destination": "Off-the-beaten-path Locations",
#         "duration": "5 days / 4 nights",
#         "description": "Discover hidden gems and lesser-known wonders in remote locations.",
#         "adult_price": 550,
#         "child_price": 275
#     },
#     {
#         "tour_name": "Festive Fiesta Discovery",
#         "destination": "Colorful Festivals",
#         "duration": "3 days / 2 nights",
#         "description": "Immerse yourself in the vibrancy of local festivals and celebrations.",
#         "adult_price": 400,
#         "child_price": 200
#     },
#     {
#         "tour_name": "Lakeside Retreat Expedition",
#         "destination": "Scenic Lakeside",
#         "duration": "4 days / 3 nights",
#         "description": "Relax and unwind in the tranquility of a scenic lakeside retreat.",
#         "adult_price": 480,
#         "child_price": 240
#     }
# ]
# tours += [
#     {
#         "tour_name": "Gastronomic Delights Discovery",
#         "destination": "Culinary Capitals",
#         "duration": "4 days / 3 nights",
#         "description": "Indulge in a gastronomic journey exploring diverse culinary delights.",
#         "adult_price": 480,
#         "child_price": 240
#     },
#     {
#         "tour_name": "Volcano Exploration Expedition",
#         "destination": "Volcanic Landscapes",
#         "duration": "6 days / 5 nights",
#         "description": "Explore the awe-inspiring landscapes and learn about volcanic formations.",
#         "adult_price": 650,
#         "child_price": 325
#     },
#     {
#         "tour_name": "Historical Marvels Trail",
#         "destination": "Ancient Architectural Wonders",
#         "duration": "5 days / 4 nights",
#         "description": "Uncover the rich history behind magnificent historical marvels.",
#         "adult_price": 550,
#         "child_price": 275
#     },
#     {
#         "tour_name": "Adventure at the Ends of the Earth",
#         "destination": "Remote Expeditions",
#         "duration": "7 days / 6 nights",
#         "description": "Embark on an adventurous journey to remote and untouched landscapes.",
#         "adult_price": 750,
#         "child_price": 375
#     },
#     {
#         "tour_name": "Tropical Rainforest Trek",
#         "destination": "Lush Rainforest",
#         "duration": "4 days / 3 nights",
#         "description": "Discover diverse flora and fauna in a lush tropical rainforest.",
#         "adult_price": 520,
#         "child_price": 260
#     },
#     {
#         "tour_name": "Wellness Retreat Escape",
#         "destination": "Tranquil Wellness Center",
#         "duration": "3 days / 2 nights",
#         "description": "Revitalize your body and mind in a serene wellness retreat.",
#         "adult_price": 420,
#         "child_price": 210
#     },
#     {
#         "tour_name": "Glacier Wonderland Adventure",
#         "destination": "Glacial Landscapes",
#         "duration": "5 days / 4 nights",
#         "description": "Explore the stunning beauty of glaciers and icy landscapes.",
#         "adult_price": 600,
#         "child_price": 300
#     },
#     {
#         "tour_name": "Vibrant Cityscape Quest",
#         "destination": "Metropolitan Adventure",
#         "duration": "4 days / 3 nights",
#         "description": "Explore the lively streets and cultural richness of a vibrant city.",
#         "adult_price": 450,
#         "child_price": 225
#     },
#     {
#         "tour_name": "Artisanal Crafts Expedition",
#         "destination": "Traditional Artisan Villages",
#         "duration": "3 days / 2 nights",
#         "description": "Discover the intricate craftsmanship and cultural heritage of artisanal villages.",
#         "adult_price": 300,
#         "child_price": 150
#     },
#     {
#         "tour_name": "Whispering Winds Retreat",
#         "destination": "Tranquil Countryside",
#         "duration": "4 days / 3 nights",
#         "description": "Rejuvenate in the peaceful ambiance of the countryside amid gentle winds.",
#         "adult_price": 400,
#         "child_price": 200
#     }
# ]
# tours += [
#     {
#         "tour_name": "Adventure in the Heartlands",
#         "destination": "Rural Exploration",
#         "duration": "5 days / 4 nights",
#         "description": "Embark on an adventurous journey through picturesque rural landscapes.",
#         "adult_price": 550,
#         "child_price": 275
#     },
#     {
#         "tour_name": "Seaside Serenity Escape",
#         "destination": "Coastal Haven",
#         "duration": "3 days / 2 nights",
#         "description": "Relax and rejuvenate in a serene seaside escape with breathtaking views.",
#         "adult_price": 400,
#         "child_price": 200
#     },
#     {
#         "tour_name": "Cultural Immersion Odyssey",
#         "destination": "Diverse Cultural Enclaves",
#         "duration": "6 days / 5 nights",
#         "description": "Immerse yourself in the traditions and customs of diverse cultural enclaves.",
#         "adult_price": 600,
#         "child_price": 300
#     },
#     {
#         "tour_name": "Majestic Mountain Expedition",
#         "destination": "Majestic Peaks",
#         "duration": "7 days / 6 nights",
#         "description": "Discover the majestic beauty and grandeur of towering mountain peaks.",
#         "adult_price": 700,
#         "child_price": 350
#     },
#     {
#         "tour_name": "Enchanted Forest Retreat",
#         "destination": "Magical Woodlands",
#         "duration": "4 days / 3 nights",
#         "description": "Explore the enchanting beauty and mystique of magical woodlands.",
#         "adult_price": 480,
#         "child_price": 240
#     },
#     {
#         "tour_name": "Riverside Adventure Quest",
#         "destination": "Scenic Riverbanks",
#         "duration": "3 days / 2 nights",
#         "description": "Embark on an adventure along scenic riversides and explore hidden treasures.",
#         "adult_price": 420,
#         "child_price": 210
#     },
#     {
#         "tour_name": "Winter Wonderland Expedition",
#         "destination": "Snowy Landscapes",
#         "duration": "6 days / 5 nights",
#         "description": "Experience the magic of winter in stunning snowy landscapes.",
#         "adult_price": 650,
#         "child_price": 325
#     },
#     {
#         "tour_name": "Epic Coastal Discovery",
#         "destination": "Coastal Marvels",
#         "duration": "5 days / 4 nights",
#         "description": "Explore the wonders and marvels of diverse coastal landscapes.",
#         "adult_price": 580,
#         "child_price": 290
#     },
#     {
#         "tour_name": "Trek to Ancient Temples",
#         "destination": "Historical Temples",
#         "duration": "4 days / 3 nights",
#         "description": "Embark on a trek to discover ancient and mystical temples.",
#         "adult_price": 520,
#         "child_price": 260
#     },
#     {
#         "tour_name": "Safari Adventure Expedition",
#         "destination": "African Savannah",
#         "duration": "7 days / 6 nights",
#         "description": "Embark on an exciting safari adventure in the African savannah.",
#         "adult_price": 750,
#         "child_price": 375
#     }
# ]
# tours += [
#     {
#         "tour_name": "Mystical Island Exploration",
#         "destination": "Remote Islands",
#         "duration": "6 days / 5 nights",
#         "description": "Uncover the mysteries of remote and uncharted islands.",
#         "adult_price": 680,
#         "child_price": 340
#     },
#     {
#         "tour_name": "Alpine Adventure Expedition",
#         "destination": "Alpine Regions",
#         "duration": "8 days / 7 nights",
#         "description": "Embark on an adventure amidst breathtaking alpine landscapes.",
#         "adult_price": 800,
#         "child_price": 400
#     },
#     {
#         "tour_name": "Serenade at Sunset",
#         "destination": "Scenic Beaches",
#         "duration": "4 days / 3 nights",
#         "description": "Experience romantic sunsets at picturesque and serene beaches.",
#         "adult_price": 450,
#         "child_price": 225
#     },
#     {
#         "tour_name": "Cultural Heritage Trail",
#         "destination": "Heritage Sites",
#         "duration": "5 days / 4 nights",
#         "description": "Explore the rich cultural heritage of ancient heritage sites.",
#         "adult_price": 600,
#         "child_price": 300
#     },
#     {
#         "tour_name": "Adventures in the Outback",
#         "destination": "Australian Outback",
#         "duration": "7 days / 6 nights",
#         "description": "Embark on thrilling adventures in the rugged Australian outback.",
#         "adult_price": 720,
#         "child_price": 360
#     },
#     {
#         "tour_name": "Tropical Paradise Getaway",
#         "destination": "Exotic Tropical Haven",
#         "duration": "3 days / 2 nights",
#         "description": "Relax and unwind in an exotic tropical paradise.",
#         "adult_price": 400,
#         "child_price": 200
#     },
#     {
#         "tour_name": "Majestic Waterfall Trek",
#         "destination": "Scenic Waterfalls",
#         "duration": "4 days / 3 nights",
#         "description": "Explore and discover majestic waterfalls hidden in natural beauty.",
#         "adult_price": 500,
#         "child_price": 250
#     },
#     {
#         "tour_name": "Adventure in the Highlands",
#         "destination": "Highland Landscapes",
#         "duration": "6 days / 5 nights",
#         "description": "Embark on an adventurous journey through picturesque highland landscapes.",
#         "adult_price": 650,
#         "child_price": 325
#     },
#     {
#         "tour_name": "Island Hopping Excursion",
#         "destination": "Island Archipelago",
#         "duration": "5 days / 4 nights",
#         "description": "Hop across stunning islands and explore their unique charms.",
#         "adult_price": 580,
#         "child_price": 290
#     },
#     {
#         "tour_name": "Enchanting Forest Retreat",
#         "destination": "Enchanted Forests",
#         "duration": "4 days / 3 nights",
#         "description": "Experience the tranquility of enchanting forests and pristine nature.",
#         "adult_price": 480,
#         "child_price": 240
#     }
# ]
# tours += [
#     {
#         "tour_name": "Mystic Mountain Voyage",
#         "destination": "Majestic Mountain Ranges",
#         "duration": "7 days / 6 nights",
#         "description": "Embark on a voyage through majestic mountain ranges and towering peaks.",
#         "adult_price": 700,
#         "child_price": 350
#     },
#     {
#         "tour_name": "Coastal Bliss Retreat",
#         "destination": "Coastal Haven",
#         "duration": "3 days / 2 nights",
#         "description": "Relax and rejuvenate in a serene coastal haven with breathtaking views.",
#         "adult_price": 400,
#         "child_price": 200
#     },
#     {
#         "tour_name": "Urban Wonders Wanderlust",
#         "destination": "City Exploration",
#         "duration": "4 days / 3 nights",
#         "description": "Explore the wonders of a bustling city and its vibrant streets.",
#         "adult_price": 450,
#         "child_price": 225
#     },
#     {
#         "tour_name": "Tranquil Oasis Odyssey",
#         "destination": "Tranquil Oasis",
#         "duration": "5 days / 4 nights",
#         "description": "Escape to a tranquil oasis and relax in peaceful serenity.",
#         "adult_price": 550,
#         "child_price": 275
#     },
#     {
#         "tour_name": "Sunset Serenade Sojourn",
#         "destination": "Coastal Retreat",
#         "duration": "3 days / 2 nights",
#         "description": "Witness mesmerizing sunsets on a serene coastal retreat.",
#         "adult_price": 350,
#         "child_price": 175
#     },
#     {
#         "tour_name": "Northern Lights Expedition",
#         "destination": "Arctic Wilderness",
#         "duration": "8 days / 7 nights",
#         "description": "Chase the ethereal beauty of the Northern Lights in the Arctic wilderness.",
#         "adult_price": 800,
#         "child_price": 400
#     },
#     {
#         "tour_name": "Ancient Ruins Adventure",
#         "destination": "Archaeological Sites",
#         "duration": "6 days / 5 nights",
#         "description": "Explore ancient ruins and uncover lost civilizations.",
#         "adult_price": 600,
#         "child_price": 300
#     },
#     {
#         "tour_name": "Jungle Safari Quest",
#         "destination": "Tropical Rainforests",
#         "duration": "5 days / 4 nights",
#         "description": "Embark on a thrilling safari adventure in lush tropical rainforests.",
#         "adult_price": 550,
#         "child_price": 275
#     },
#     {
#         "tour_name": "Spiritual Sanctuary Sojourn",
#         "destination": "Sacred Temples and Monasteries",
#         "duration": "7 days / 6 nights",
#         "description": "Find solace and spirituality in serene temples and monastic retreats.",
#         "adult_price": 700,
#         "child_price": 350
#     },
#     {
#         "tour_name": "Whale Watching Wonders",
#         "destination": "Coastal Waters",
#         "duration": "2 days / 1 night",
#         "description": "Witness the majestic beauty of whales in their natural habitat.",
#         "adult_price": 250,
#         "child_price": 125
#     }
# ]
# tours += [
#     {
#         "tour_name": "Desert Mirage Trek",
#         "destination": "Sandy Dunes",
#         "duration": "4 days / 3 nights",
#         "description": "Explore the mystical allure of the desert's sandy dunes.",
#         "adult_price": 450,
#         "child_price": 225
#     },
#     {
#         "tour_name": "Hidden Gems Excursion",
#         "destination": "Off-the-beaten-path Locations",
#         "duration": "5 days / 4 nights",
#         "description": "Discover hidden gems and lesser-known wonders in remote locations.",
#         "adult_price": 550,
#         "child_price": 275
#     },
#     {
#         "tour_name": "Festive Fiesta Discovery",
#         "destination": "Colorful Festivals",
#         "duration": "3 days / 2 nights",
#         "description": "Immerse yourself in the vibrancy of local festivals and celebrations.",
#         "adult_price": 400,
#         "child_price": 200
#     },
#     {
#         "tour_name": "Lakeside Retreat Expedition",
#         "destination": "Scenic Lakeside",
#         "duration": "4 days / 3 nights",
#         "description": "Relax and unwind in the tranquility of a scenic lakeside retreat.",
#         "adult_price": 480,
#         "child_price": 240
#     },
#     {
#         "tour_name": "Gastronomic Delights Discovery",
#         "destination": "Culinary Capitals",
#         "duration": "4 days / 3 nights",
#         "description": "Indulge in a gastronomic journey exploring diverse culinary delights.",
#         "adult_price": 480,
#         "child_price": 240
#     },
#     {
#         "tour_name": "Volcano Exploration Expedition",
#         "destination": "Volcanic Landscapes",
#         "duration": "6 days / 5 nights",
#         "description": "Explore the awe-inspiring landscapes and learn about volcanic formations.",
#         "adult_price": 650,
#         "child_price": 325
#     },
#     {
#         "tour_name": "Historical Marvels Trail",
#         "destination": "Ancient Architectural Wonders",
#         "duration": "5 days / 4 nights",
#         "description": "Uncover the rich history behind magnificent historical marvels.",
#         "adult_price": 550,
#         "child_price": 275
#     },
#     {
#         "tour_name": "Adventure at the Ends of the Earth",
#         "destination": "Remote Expeditions",
#         "duration": "7 days / 6 nights",
#         "description": "Embark on an adventurous journey to remote and untouched landscapes.",
#         "adult_price": 750,
#         "child_price": 375
#     },
#     {
#         "tour_name": "Tropical Rainforest Trek",
#         "destination": "Lush Rainforest",
#         "duration": "4 days / 3 nights",
#         "description": "Discover diverse flora and fauna in a lush tropical rainforest.",
#         "adult_price": 520,
#         "child_price": 260
#     },
#     {
#         "tour_name": "Wellness Retreat Escape",
#         "destination": "Tranquil Wellness Center",
#         "duration": "3 days / 2 nights",
#         "description": "Revitalize your body and mind in a serene wellness retreat.",
#         "adult_price": 420,
#         "child_price": 210
#     }
# ]

tour_dates = [
    {
        "departure_datetime": "2024-1-01",
    },
    {
        "departure_datetime": "2024-1-02",
    },
    {
        "departure_datetime": "2024-1-03",
    },
    {
        "departure_datetime": "2024-1-04",
    },
    {
        "departure_datetime": "2024-1-05",
    },
    {
        "departure_datetime": "2024-1-06",
    },
    {
        "departure_datetime": "2024-1-07",
    },
    {
        "departure_datetime": "2024-1-08",
    },
    {
        "departure_datetime": "2024-1-09",
    },
    {
        "departure_datetime": "2024-1-10",
    },
    {
        "departure_datetime": "2024-1-11",
    },
    {
        "departure_datetime": "2024-1-12",
    },
    {
        "departure_datetime": "2024-1-13",
    },
    {
        "departure_datetime": "2024-1-14",
    },
    {
        "departure_datetime": "2024-1-15",
    },
    {
        "departure_datetime": "2024-1-16",
    },
    {
        "departure_datetime": "2024-1-17",
    },
    {
        "departure_datetime": "2024-1-18",
    },
    {
        "departure_datetime": "2024-1-19",
    },
    {
        "departure_datetime": "2024-1-20",
    },
    {
        "departure_datetime": "2024-1-21",
    },
    {
        "departure_datetime": "2024-1-22",
    },
    {
        "departure_datetime": "2024-1-23",
    },
    {
        "departure_datetime": "2024-1-24",
    },
    {
        "departure_datetime": "2024-1-25",
    },
    {
        "departure_datetime": "2024-1-26",
    },
    {
        "departure_datetime": "2024-1-27",
    },
    {
        "departure_datetime": "2024-1-28",
    },
    {
        "departure_datetime": "2024-1-29",
    },
    {
        "departure_datetime": "2024-1-30",
    },
    {
        "departure_datetime": "2024-1-31",
    },
    {
        "departure_datetime": "2024-2-01",
    },
    {
        "departure_datetime": "2024-2-02",
    },
    {
        "departure_datetime": "2024-2-03",
    },
    {
        "departure_datetime": "2024-2-04",
    },
    {
        "departure_datetime": "2024-2-05",
    },
    {
        "departure_datetime": "2024-2-06",
    },
]


for tour in tours:
    tour["duration"] = int(tour["duration"][0])
    # print(tour)
    # tour_insert= schemas.TourCreate(tour)
    # tour_insert= schemas.TourCreate(tour_name=tour["tour_name"], destination=tour["destination"], duration=tour["duration"], description=tour["description"], adult_price=tour["adult_price"], child_price=tour["child_price"])
    # tour_insert.tour_name = tour["tour_name"]
    # tour_insert.destination = tour["destination"]
    # tour_insert.duration = tour["duration"]
    # tour_insert.description = tour["description"]
    # tour_insert.adult_price = tour["adult_price"]
    # tour_insert.child_price = tour["child_price"]
    # print(tour_insert)
    tour["name"] = tour["tour_name"]
    del tour["tour_name"]
    tour_insert = schemas.TourCreate(**tour)
    crud_tour_insert = crud_tour.create_tour(tour=tour_insert)

    for date in tour_dates:
        date["tour_id"] = crud_tour_insert.id

        # date["return_datetime"] = datetime.datetime.strptime(date["departure_datetime"], "") + datetime.timedelta(
        #     days=tour_insert.duration)
        # date["return_datetime"] = datetime.datetime.strptime(date["departure_datetime"], "%Y-%m-%d %H:%M:%S") + datetime.timedelta(
        #     days=tour_insert.duration)
        # print(type(date["departure_datetime"]))
        # date["departure_datetime"] = datetime.strptime(date["departure_datetime"], "%Y-%m-%d %H:%M:%S")
        date["departure_datetime"] = datetime.date(datetime.now()) + timedelta(days=random.randint(1, 50))
        # date["departure_datetime"]= date["departure_datetime"]

        date["return_datetime"] = date["departure_datetime"] + timedelta(days=tour_insert.duration-1)
        # print(date)
        # date_insert = schemas.TourDateCreate(tour_id=date["tour_id"], departure_datetime=date["departure_datetime"], return_datetime=date["return_datetime"])
        date_insert = schemas.TourDateCreate(**date)
        crud_tour_date.create_tour_date(tour_date=date_insert)

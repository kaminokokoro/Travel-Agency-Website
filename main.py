import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse

from backend.routes.login import router_login
from backend.routes.user import router_user

from backend.routes.hotel import router_hotel
from backend.routes.hotel_service import router_hotel_service
from backend.routes.hotel_booking import router_hotel_booking
from backend.routes.user_hotel_rating import router_user_hotel_rating

from backend.routes.tour import router_tour
from backend.routes.tour_date import router_tour_date
from backend.routes.tour_booking import router_tour_booking
from backend.routes.user_tour_rating import router_user_tour_rating

from backend.routes.flight import router_flight
from backend.routes.flight_provider import router_flight_provider
from backend.routes.flight_booking import router_flight_booking
from backend.routes.flight_ticket import router_flight_ticket
from backend.routes.user_flight_provider_rating import router_user_flight_provider_rating


# REST API Settings
app = FastAPI(description="Sample Server")

# API Routers



app.include_router(router_login, prefix='', tags=['Login'])
app.include_router(router_user, prefix='/user',tags=['User'])

app.include_router(router_hotel, prefix='/hotel',tags=['Hotel'])
app.include_router(router_hotel_service, prefix='/hotel/service',tags=['Hotel Service'])
app.include_router(router_hotel_booking, prefix='/hotel/booking',tags=['Hotel Booking'])
app.include_router(router_user_hotel_rating, prefix='/hotel-rating',tags=['User Hotel Rating'])

app.include_router(router_tour, prefix='/tour',tags=['Tour'])
app.include_router(router_tour_date, prefix="/tour/date", tags=["tour date"])
app.include_router(router_tour_booking, prefix="/tour/booking", tags=["tour booking"])
app.include_router(router_user_tour_rating, prefix="/tour/rating", tags=["tour rating"])

app.include_router(router_flight, prefix="/flight", tags=["flight"])
app.include_router(router_flight_provider, prefix="/flight/provider", tags=["flight provider"])
app.include_router(router_flight_booking, prefix="/flight/booking", tags=["flight booking"])
app.include_router(router_flight_ticket, prefix="/flight/ticket", tags=["flight ticket"])
app.include_router(router_user_flight_provider_rating, prefix="/flight/rating", tags=["flight rating"])




# Root API
@app.get('/')
def root() -> JSONResponse:
    return JSONResponse(status_code=200,
                        content={
                            "message": "Welcome to Sample Server"})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level='debug', reload=True)
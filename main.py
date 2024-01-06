import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse

from backend.routes.hotel import router_hotel
from backend.routes.login import router_login
from backend.routes.tour_date import router_tour_date
from backend.routes.user import router_user
from backend.routes.tour import router_tour
from backend.routes.user_hotel_rating import router_user_hotel_rating
from backend.routes.user_tour_rating import router_user_tour_rating
from backend.routes.tour_booking import router_tour_booking
from backend.routes.flight import router_flight
# REST API Settings
app = FastAPI(description="Sample Server")

# API Routers



app.include_router(router_login, prefix='', tags=['Login'])
app.include_router(router_user, prefix='/user',tags=['User'])
app.include_router(router_hotel, prefix='/hotel',tags=['Hotel'])
app.include_router(router_user_hotel_rating, prefix='/hotel-rating',tags=['User Hotel Rating'])
app.include_router(router_tour, prefix='/tour',tags=['Tour'])
app.include_router(router_tour_date, prefix="/tour/date", tags=["tour date"])
app.include_router(router_user_tour_rating, prefix="/tour/rating", tags=["tour rating"])
app.include_router(router_tour_booking, prefix="/tour/booking", tags=["tour booking"])
app.include_router(router_flight, prefix="/flight", tags=["flight"])




# Root API
@app.get('/')
def root() -> JSONResponse:
    return JSONResponse(status_code=200,
                        content={
                            "message": "Welcome to Sample Server"})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level='debug', reload=True)
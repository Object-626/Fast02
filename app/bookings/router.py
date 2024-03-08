from fastapi import APIRouter, Depends, Request
from app.bookings.dao import BookingDAO
from app.users.model import Users
from app.users.dependencies import get_current_user


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingDAO.find_all(user_id=user.id)




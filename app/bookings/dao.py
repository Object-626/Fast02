from app.bookings.model import Bookings
from app.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Bookings

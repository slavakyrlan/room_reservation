from app.crud.base import CRUDBase
from app.models.reservation import Reservation
from datetime import datetime
from typing import Optional
from sqlalchemy import and_, between, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

reservation_crud = CRUDBase(Reservation)


class CRUDReservation(CRUDBase):
    async def get_reservations_at_the_same_time(
        self,
        # Через * обозначим что все дальнейшие параметры должны передаваться по
        # ключу. И расположим параметры со значением по-умолчанию перед
        # значениями без параметра по-умолчанию
        *,
        from_reserve: datetime,
        to_reserve: datetime,
        meetingroom_id: int,
        # Опциональный параметр - id объекта бронирования
        reservation_id: Optional[int] = None,
        session: AsyncSession,
    ) -> list[Reservation]:
        reservations = await session.execute(
            select(Reservation).where(
                Reservation.meetingroom_id == meetingroom_id,
                and_(
                    from_reserve <= Reservation.to_reserve,
                    to_reserve >= Reservation.from_reserve
                )
            )
        )
        reservations = reservations.scalars().all()
        return reservations


reservation_crud = CRUDReservation(Reservation)

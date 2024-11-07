from sqlalchemy import select
from model.restorant_model import RestorantModel
from repository.base_repository import BaseRepository


class RestorantRepository(BaseRepository):
    async def get_restorant_list(self):
        pass

    async def get_restorant_by_id(self, restorant_id: str) -> RestorantModel:
        stmt = select(RestorantModel).where(RestorantModel.restorant_id == restorant_id)

        res = await self.session.execute(stmt)
        res = res.scalar()
        return res

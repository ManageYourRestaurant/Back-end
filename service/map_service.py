from repository.restorant_repository import RestorantRepository
from schema.restorant_schema import Restorant
from service.base_service import BaseService


class MapService(BaseService):
    def __init__(self, session):
        super().__init__(session)
        self.restorant_repository = RestorantRepository(session=self.session)

    async def get_restorant_list(self):
        pass

    async def get_restorant_by_id(self, restorant_id: str) -> Restorant:
        restorant = await self.restorant_repository.get_restorant_by_id(restorant_id=restorant_id)
        return Restorant.model_validate(restorant)

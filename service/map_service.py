from repository.restorant_repository import RestorantRepository
from service.base_service import BaseService


class MapSerice(BaseService):
    async def get_retorant_list(self):
        restorant_repository = RestorantRepository(session=self.session)
        pass

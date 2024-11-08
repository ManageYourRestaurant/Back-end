from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.db_config import get_async_session
from schema.restorant_schema import RestorantResponse
from service.map_service import MapService

restorant_router = APIRouter()


# 해당지도내에서 가게들을 검색해서 보여주기(나중에 조건을 추가할 것)
@restorant_router.get("/get/restorant_list")
async def get_restorant_list():
    return True


@restorant_router.get("/restorant", description="가게 하나를 리턴", response_model=RestorantResponse)
async def get_restorant_by_id(restorant_id: str, session: AsyncSession = Depends(get_async_session)) -> RestorantResponse:
    res = await MapService(session=session).get_restorant_by_id(restorant_id=restorant_id)
    return res

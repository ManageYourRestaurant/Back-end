from fastapi import APIRouter

map_router = APIRouter()


# 해당지도내에서 가게들을 검색해서 보여주기(나중에 조건을 추가할 것)
@map_router.get("/get/restorant_list")
async def get_restorant_list():
    return True


#

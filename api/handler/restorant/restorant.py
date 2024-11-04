from fastapi import APIRouter

restorant_router = APIRouter()


# 식당 전체 정보 가져오기
@restorant_router.get("/get")
async def get_restorant():
    return True


# 메뉴가져오기

# 태그 가져오기

# 식당 댓글 가져오기

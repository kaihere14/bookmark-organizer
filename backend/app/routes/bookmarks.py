from fastapi import APIRouter

router = APIRouter(
    prefix="/bookmarks",
    tags=["bookmarks"],
)

@router.get("/")
def get_bookmarks():
    return {"message": "Get bookmarks"}
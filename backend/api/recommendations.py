from fastapi import APIRouter

router = APIRouter()

@router.get("/recommendations")
def recommendations():

    return {
        "message": "Recommendation API working"
    }
from fastapi import APIRouter, Body
from api.utils.database import save_feedback

router = APIRouter(prefix="/feedback", tags=["Feedback"])

@router.post("/")
async def submit_feedback(
    query: str = Body(...),
    answer: str = Body(...),
    rating: float = Body(..., ge=0, le=1)
):
    feedback = {"query": query, "answer": answer, "rating": rating}
    save_feedback(feedback)
    return {"status": "success", "message": "Feedback logged"}

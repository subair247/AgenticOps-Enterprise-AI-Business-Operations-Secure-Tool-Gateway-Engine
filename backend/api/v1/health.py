from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "healthy", "service": "AI-Ops Agent Platform Backend"}
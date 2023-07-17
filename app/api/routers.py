from fastapi import APIRouter

from app.api.endpoints import insurance_router

main_router = APIRouter()
main_router.include_router(
    insurance_router,
    tags=['Insurance'],
)

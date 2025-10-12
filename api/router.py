from fastapi import APIRouter
from api.v1.solvers import router as solve_router

router = APIRouter(prefix="/v1", tags=["v1"])
router.include_router(solve_router)
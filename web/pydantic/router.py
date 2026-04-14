from fastapi import APIRouter
from . import pydantic

router = APIRouter(
    prefix="/pydantic" 
)

route_mappings = [
    (pydantic.router, "/register"),
]

for sub_router, sub_prefix in route_mappings:
    router.include_router(sub_router, prefix=sub_prefix, tags=["Pydantic"])

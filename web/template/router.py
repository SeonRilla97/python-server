from fastapi import APIRouter
from . import jinja


router = APIRouter(
    prefix="/template" # 공통 경로
)

# [리팩토링] 라우터 객체와 경로를 리스트로 매핑하여 일괄 등록
route_mappings = [
    (jinja.router, "/jinja"),
]

for sub_router, sub_prefix in route_mappings:
    router.include_router(sub_router, prefix=sub_prefix, tags=["template"])
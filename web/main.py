from fastapi import FastAPI
from swagger.swagger import router as swagger_router
from request.router import router as request_router
from response.router import router as response_router
from template.router import router as template_router
from pydantic.router import router as pydantic_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# FastAPI Instance 생성
app = FastAPI()

templates = Jinja2Templates(directory="./static/templates")

# 라우터 장착
app.include_router(swagger_router)
app.include_router(request_router)
app.include_router(response_router)
app.include_router(template_router)
app.include_router(pydantic_router)


# 라우터
'''
유저가 서버에 요청할 시
FastAPI는 아래와 같이 동작한다.
 1. Path 기준으로 라우터를 찾는다.
 2. 응답시 Default로 application/json을 반환한다.

'''

@app.get("/health",
tags=["health"])
async def health_check():
    return {"status": "OK"}
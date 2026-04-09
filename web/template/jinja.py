from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="./static/templates")

class Item(BaseModel):
    name: str
    price: int

@router.get("/items/{id}", response_class=HTMLResponse)
async def template_item(request: Request, id: str, q: str | None = None):
    '''
    template engine 사용 시 반드시 request 선언 필수
    '''

    item = Item(
        name="test_item",
        price=1000
    )

    item_dict = item.model_dump()
    return templates.TemplateResponse(
        request=request,
        name="item.html",
        context={"id": id, "item": item_dict}
    )
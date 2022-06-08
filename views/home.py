import fastapi
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = fastapi.APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get('/about')
def about():
    return {}

import fastapi
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from views import home, account, packages

app = fastapi.FastAPI()
app.include_router(home.router)
app.include_router(account.router)
# app.include_router(packages.router)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

if __name__ == "__main__":
    uvicorn.run(app, reload=True)

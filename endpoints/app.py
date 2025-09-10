import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from endpoints.get_query import GetQuerys
from services.logger.logger import Logger

logger = Logger.get_logger(index="endpoint-logs")


app = FastAPI()
templates = Jinja2Templates(directory="../endpoints")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serves the HTML form page.
    """
    logger.info(f"Serving {request.url}")
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process", response_class=HTMLResponse)
async def process_word(request: Request, user_word: str = Form(...)):
    """
    Receives the word from the form and processes it.
    """
    logger.info(f"Received word {user_word}")
    processed_message = GetQuerys(request).results()
    return {"request": request, "message": processed_message}
@app.get("/is_bds")
async def read_root():
    return GetQuerys(None).get_dbs_classification()

if __name__ == '__main__':
    uvicorn.run(app, host = "localhost", port=8010)
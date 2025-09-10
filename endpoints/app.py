import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from endpoints.get_query import GetQuerys



app = FastAPI()
templates = Jinja2Templates(directory="../endpoints")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serves the HTML form page.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process", response_class=HTMLResponse)
async def process_word(request: Request, user_word: str = Form(...)):
    """
    Receives the word from the form and processes it.
    """

    processed_message = GetQuerys(request).results()
    return templates.TemplateResponse("result.html", {"request": request, "message": processed_message})

if __name__ == '__main__':
    uvicorn.run(app, host = "localhost", port=8010)
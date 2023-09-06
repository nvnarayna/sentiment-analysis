from models import Nlp
from nlp import analyze_sentiment
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/_app", StaticFiles(directory="./build/_app"), name="static")


templates = Jinja2Templates(directory="./build")

#/workspaces/codespaces-blank/server/build/index.html
@app.get("/",response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post('/api/nlp')
async def nlp(content: Nlp):
    sentiment = analyze_sentiment(content)
    print(sentiment.sentiment)
    return sentiment.res()



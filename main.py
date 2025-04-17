from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import google.generativeai as genai
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": None})

@app.post("/", response_class=HTMLResponse)
async def post_chat(request: Request, prompt: str = Form(...)):
    response = model.generate_content(prompt)
    return templates.TemplateResponse("index.html", {"request": request, "response": response.text})

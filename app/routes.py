from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/generate", response_class=HTMLResponse)
async def generate_comic(request: Request,
    story_idea: str = Form(""),
    main_character: str = Form(""),
    setting: str = Form(""),
    comic_style: str = Form("Cute Cartoon"),
    number_of_panels: str = Form("5"),
    tone: str = Form("")
):
    print("RECEIVED:", story_idea, main_character)

    try:
        num = int(str(number_of_panels).split()[0])
    except:
        num = 5

    from app.image_generator import generate_image

    panels = []
    for i in range(1, num+1):
        prompt = f"{main_character} {story_idea} in {setting}, {comic_style} style"
        try:
            generate_image(prompt, f"panel_{i}.png")
        except Exception as e:
            print(e)

        panels.append({
            "number": i,
            "title": f"Panel {i}",
            "text": f"{main_character} - {story_idea} - scene {i}",
            "image_path": f"/static/panels/panel_{i}.png",
            "scene": f"Scene {i}"
        })

    return templates.TemplateResponse("comic_preview.html", {
        "request": request,
        "panels": panels,
        "story_prompt": story_idea
    })

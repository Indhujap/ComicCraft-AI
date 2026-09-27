from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path
app = FastAPI()
Path('static/panels').mkdir(parents=True, exist_ok=True)
Path('static/exports').mkdir(parents=True, exist_ok=True)
app.mount('/static', StaticFiles(directory='static'), name='static')
@app.get('/', response_class=HTMLResponse)
async def home():
    return '<h1>ComicCraft AI - Person 4 Jeevanantham</h1><form action=\"/generate\" method=\"post\">Story: <input name=\"story_idea\" value=\"monkey\"><br>Character: <input name=\"main_character\" value=\"monkey\"><br>Setting: <input name=\"setting\" value=\"village\"><br><button>Generate</button></form>'
@app.post('/generate', response_class=HTMLResponse)
async def generate(story_idea: str = Form(''), main_character: str = Form(''), setting: str = Form('')):
    from app.image_generator import generate_image
    for i in range(1,6):
        generate_image(f'{main_character} {story_idea}', f'panel_{i}.png')
    html = '<h1>Generated!</h1>'
    for i in range(1,6):
        html += f'<img src=\"/static/panels/panel_{i}.png\" width=\"200\">'
    return HTMLResponse(html + '<br><a href=\"/\">Back</a>')

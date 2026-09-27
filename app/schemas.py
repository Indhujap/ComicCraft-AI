from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class PromptRequest(BaseModel):
    prompt: str
    num_pages: Optional[int] = 6
    style: Optional[str] = "manga"
    genre: Optional[str] = "adventure"

class ImageRequest(BaseModel):
    prompt: str
    filename: Optional[str] = "panel.png"

class LayoutRequest(BaseModel):
    image_paths: List[str]
    output_filename: Optional[str] = "comic_layout.png"

class ExportRequest(BaseModel):
    story_data: Dict[str, Any]
    filename: Optional[str] = "comic.pdf"

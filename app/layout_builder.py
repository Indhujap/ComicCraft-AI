from pathlib import Path
from PIL import Image
from typing import List

def build_comic_layout(image_paths: List[Path], output_filename: str = "comic_layout.png") -> Path:
    """
    Temporary stub - joins images vertically into one comic page.
    Replace with real layout logic later.
    """
    from app.config import EXPORTS_DIR

    if not image_paths:
        # return a blank if no images
        blank = Image.new('RGB', (512, 512), color=(255,255,255))
        out = EXPORTS_DIR / output_filename
        blank.save(out)
        return out

    images = [Image.open(p) for p in image_paths if Path(p).exists()]
    if not images:
        images = [Image.new('RGB', (512, 512), color=(200,200,200))]

    # simple vertical stack
    widths, heights = zip(*(i.size for i in images))
    max_width = max(widths)
    total_height = sum(heights)

    new_im = Image.new('RGB', (max_width, total_height))
    y_offset = 0
    for im in images:
        new_im.paste(im, (0, y_offset))
        y_offset += im.size[1]

    output_path = EXPORTS_DIR / output_filename
    new_im.save(output_path)
    return output_path

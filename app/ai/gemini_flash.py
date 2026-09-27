# Fix for ImportError: generate_outline
import os

def generate_outline(prompt: str, num_pages: int = 6) -> dict:
    """
    Temporary stub. Replace with real Gemini Flash call later.
    """
    return {
        "title": "Generated Comic Outline",
        "prompt": prompt,
        "pages": [
            {"page": i+1, "scene": f"Scene {i+1} for: {prompt[:50]}"}
            for i in range(num_pages)
        ]
    }

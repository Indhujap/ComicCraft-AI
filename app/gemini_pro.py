# Fix for ImportError: generate_story

def generate_story(outline: dict) -> dict:
    """
    Temporary stub. Replace with real Gemini Pro call later.
    """
    return {
        "title": outline.get("title", "Comic Story"),
        "outline": outline,
        "story": "This is a dummy story generated because real Gemini API is not connected yet.",
        "dialogues": ["Hello!", "Let's adventure!"] * 3
    }

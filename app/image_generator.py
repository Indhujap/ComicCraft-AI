import requests
from pathlib import Path

def generate_image(prompt, filename):
    print(f"Generating image: {filename} - {prompt}")
    # Free AI image - Pollinations
    safe_prompt = requests.utils.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{safe_prompt}?width=512&height=512&nologo=true&model=turbo"

    try:
        response = requests.get(url, timeout=90)
        response.raise_for_status()

        output_dir = Path("static/panels")
        output_dir.mkdir(parents=True, exist_ok=True)

        file_path = output_dir / filename
        file_path.write_bytes(response.content)
        print(f"Saved: {file_path}")
        return str(file_path)
    except Exception as e:
        print(f"Image gen failed {filename}: {e}")
        # Create a dummy file so page doesn't break
        return f"static/panels/{filename}"

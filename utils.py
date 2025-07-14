import os
import re
import json

def clean_text(text):
    """
    Optional: Cleans text by removing extra spaces, links, or markdown if needed.
    Currently basic – can be extended as required.
    """
    text = re.sub(r'\s+', ' ', text)  # Collapse multiple spaces/newlines
    text = re.sub(r'http\S+', '', text)  # Remove URLs (if not needed)
    return text.strip()


def save_persona(username, persona_text, folder="personas"):
    """
    Saves the generated persona to a .txt file inside the personas/ directory.
    """
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, f"{username}_persona.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(persona_text)

    print(f"[INFO] Persona written to: {file_path}")


def save_raw_data(username, user_data, folder="sample_data"):
    """
    Optional: Save raw scraped Reddit data to a JSON file for debugging or reuse.
    """
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, f"{username}_raw.json")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(user_data, f, indent=2, ensure_ascii=False)

    print(f"[INFO] Raw data saved to: {file_path}")

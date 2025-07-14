import sys
import os
from urllib.parse import urlparse

from reddit_scraper import get_user_data
from persona_builder import generate_persona
from utils import save_persona

def extract_username(url):
    """Extract Reddit username from URL."""
    parsed = urlparse(url)
    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) >= 2 and path_parts[0] == "user":
        return path_parts[1]
    else:
        raise ValueError("Invalid Reddit user URL.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python persona_generator.py <reddit_user_url>")
        return

    reddit_url = sys.argv[1]
    try:
        username = extract_username(reddit_url)
        print(f"[INFO] Extracted username: {username}")

        print("[INFO] Scraping Reddit data...")
        user_data = get_user_data(username)

        if not user_data:
            print(f"[WARN] No posts/comments found for user: {username}")
            return

        print("[INFO] Generating persona using Gemini...")
        persona_text = generate_persona(user_data)

        print("[INFO] Saving persona...")
        save_persona(username, persona_text)

        print(f"[SUCCESS] Persona saved to: personas/{username}_persona.txt")

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()

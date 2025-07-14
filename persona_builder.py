import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Load API key from .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Choose model (you can switch to "gemini-1.5-flash" for faster responses)
model = genai.GenerativeModel("gemini-1.5-flash")


def format_prompt(user_data):
    """
    Builds the prompt string to send to Gemini from Reddit post/comment data.
    """
    prompt = (
        "You are a personality analyst. Based on the following Reddit posts and comments, "
        "generate a user persona. Include: interests, personality traits, writing style, beliefs/values, "
        "frequently discussed topics, and anything else meaningful. For each trait, include a direct quote and its source URL.\n\n"
        "Format output cleanly using labeled sections.\n\n"
        "=== Reddit Activity ===\n"
    )

    for i, entry in enumerate(user_data, start=1):
        prefix = "Post" if entry["type"] == "post" else "Comment"
        text = entry["text"].strip().replace("\n", " ")
        url = entry["url"]
        prompt += f"{i}. [{prefix}] {text}\n(Source: {url})\n\n"

    return prompt


def generate_persona(user_data):
    """
    Calls Gemini API with user data and returns the persona text.
    """
    prompt = format_prompt(user_data)

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print(f"[ERROR] Gemini API failed: {e}")
        return "[ERROR] Could not generate persona due to an API error."

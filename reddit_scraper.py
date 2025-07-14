import praw
import os
from dotenv import load_dotenv

load_dotenv()

# Load Reddit API credentials
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

def get_user_data(username, limit=50):
    """
    Fetch latest posts and comments from a Reddit user.
    Returns a list of dicts with 'type', 'text', and 'url'.
    """
    result = []

    try:
        redditor = reddit.redditor(username)

        # Fetch comments
        for comment in redditor.comments.new(limit=limit):
            result.append({
                "type": "comment",
                "text": comment.body,
                "url": f"https://www.reddit.com{comment.permalink}"
            })

        # Fetch posts
        for post in redditor.submissions.new(limit=limit):
            text = post.title + "\n\n" + (post.selftext or "")
            result.append({
                "type": "post",
                "text": text,
                "url": f"https://www.reddit.com{post.permalink}"
            })

    except Exception as e:
        print(f"[ERROR] Failed to fetch data for u/{username}: {e}")

    return result

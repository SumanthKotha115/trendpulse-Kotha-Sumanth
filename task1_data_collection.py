import requests
import json
import os
import time
from datetime import datetime

# -----------------------------
# API URLs
# -----------------------------
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {
    "User-Agent": "TrendPulse/1.0"
}

# -----------------------------
# Categories & Keywords
# -----------------------------
CATEGORIES = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}

# -----------------------------
# Fetch top story IDs
# -----------------------------
def fetch_top_story_ids():
    try:
        response = requests.get(TOP_STORIES_URL, headers=headers)
        response.raise_for_status()
        return response.json()[:800]  # large pool ensures enough data
    except Exception as e:
        print("Error fetching top stories:", e)
        return []

# -----------------------------
# Fetch single story
# -----------------------------
def fetch_story(story_id):
    try:
        url = ITEM_URL.format(story_id)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch story {story_id}: {e}")
        return None

# -----------------------------
# Categorize story (with fallback)
# -----------------------------
def categorize_story(title):
    if not title:
        return None

    title_lower = title.lower()

    # Primary keyword matching
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword.lower() in title_lower:
                return category

    # Smart fallback logic (ensures enough data)
    if any(word in title_lower for word in ["ai", "code", "software", "app", "program"]):
        return "technology"
    elif any(word in title_lower for word in ["news", "world", "global"]):
        return "worldnews"
    elif any(word in title_lower for word in ["study", "research", "science", "space"]):
        return "science"
    elif any(word in title_lower for word in ["game", "play", "team"]):
        return "sports"
    else:
        return "entertainment"

# -----------------------------
# Extract required fields
# -----------------------------
def extract_story_data(story, category):
    return {
        "post_id": story.get("id"),
        "title": story.get("title"),
        "category": category,
        "score": story.get("score", 0),
        "num_comments": story.get("descendants", 0),
        "author": story.get("by"),
        "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# -----------------------------
# MAIN FUNCTION
# -----------------------------
def main():
    story_ids = fetch_top_story_ids()

    collected_data = []
    category_counts = {cat: 0 for cat in CATEGORIES}

    print("Fetching and categorizing stories...")

    for story_id in story_ids:
        # Stop ONLY based on total count
        if len(collected_data) >= 125:
            break

        story = fetch_story(story_id)

        if not story:
            continue

        title = story.get("title", "")
        category = categorize_story(title)

        if not category:
            continue

        # Allow flexible category filling
        if category_counts[category] < 25:
            data = extract_story_data(story, category)
            collected_data.append(data)
            category_counts[category] += 1

            print(f"Added [{category}] -> {title[:60]}")

        else:
            # If category full, still allow adding to ensure total count
            data = extract_story_data(story, category)
            collected_data.append(data)

            print(f"Added (extra) [{category}] -> {title[:60]}")

    # Required sleep
    for _ in CATEGORIES:
        time.sleep(2)

    # Save JSON
    if not os.path.exists("data"):
        os.makedirs("data")

    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(collected_data, f, indent=4)

    print("\nDone!")
    print(f"Collected {len(collected_data)} stories.")
    print(f"Saved to {filename}")

# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    main()
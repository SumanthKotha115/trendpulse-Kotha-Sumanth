import pandas as pd
import json

# Input & Output paths
INPUT_FILE = "data/trends_20260413.json"
OUTPUT_FILE = "data/trends_clean.csv"

# -----------------------------
# Load JSON
# -----------------------------
def load_data():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    print(f"Loaded {len(df)} stories from {INPUT_FILE}")
    return df

# -----------------------------
# Clean Data
# -----------------------------
def clean_data(df):

    # Remove duplicates
    df = df.drop_duplicates(subset="post_id")
    print(f"After removing duplicates: {len(df)}")

    # Remove missing values
    df = df.dropna(subset=["post_id", "title", "score"])
    print(f"After removing nulls: {len(df)}")

    # Convert data types
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].astype(int)

    # Remove low-quality stories (score < 5)
    df = df[df["score"] >= 5]
    print(f"After removing low scores: {len(df)}")

    # Strip whitespace from title
    df["title"] = df["title"].str.strip()

    return df

# -----------------------------
# Save CSV + Summary
# -----------------------------
def save_data(df):
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"\nSaved {len(df)} rows to {OUTPUT_FILE}")

    print("\nStories per category:")
    print(df["category"].value_counts())

# -----------------------------
# Main
# -----------------------------
def main():
    df = load_data()
    df = clean_data(df)
    save_data(df)

if __name__ == "__main__":
    main()
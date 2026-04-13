import json
import pandas as pd
import os

# Path to JSON file (from Task 1)
INPUT_FILE = "data/trends_20260413.json"

# Output CSV file
OUTPUT_FILE = "data/cleaned_trends.csv"
def load_data():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
def convert_to_dataframe(data):
    df = pd.DataFrame(data)
    return df
def clean_data(df):
    # Remove duplicates based on post_id
    df = df.drop_duplicates(subset="post_id")

    # Fill missing values
    df["score"] = df["score"].fillna(0)
    df["num_comments"] = df["num_comments"].fillna(0)
    df["author"] = df["author"].fillna("unknown")

    # Remove rows with empty title
    df = df[df["title"].notnull()]

    # Convert score & comments to integer
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].astype(int)

    return df
def save_to_csv(df):
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Cleaned data saved to {OUTPUT_FILE}")
def main():
    print("Loading data...")
    data = load_data()

    print("Converting to DataFrame...")
    df = convert_to_dataframe(data)

    print("Cleaning data...")
    df = clean_data(df)

    print("Saving to CSV...")
    save_to_csv(df)

    print("Done!")
    print(f"Total rows after cleaning: {len(df)}")

if __name__ == "__main__":
    main()
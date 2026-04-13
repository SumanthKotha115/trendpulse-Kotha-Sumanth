import pandas as pd
import numpy as np

INPUT_FILE = "data/trends_clean.csv"
OUTPUT_FILE = "data/trends_analysed.csv"

# -----------------------------
# 1 — Load and Explore
# -----------------------------
def load_data():
    df = pd.read_csv(INPUT_FILE)

    print("Loaded data:", df.shape)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nBasic averages:")
    print("Average score:", df["score"].mean())
    print("Average comments:", df["num_comments"].mean())

    return df

# -----------------------------
# 2 — NumPy Analysis
# -----------------------------
def numpy_analysis(df):
    scores = np.array(df["score"])

    print("\n--- NumPy Stats ---")
    print("Mean score:", np.mean(scores))
    print("Median score:", np.median(scores))
    print("Std deviation:", np.std(scores))
    print("Max score:", np.max(scores))
    print("Min score:", np.min(scores))

    # Category with most stories
    most_category = df["category"].value_counts().idxmax()
    most_count = df["category"].value_counts().max()
    print(f"Most stories in: {most_category} ({most_count} stories)")

    # Most commented story
    top_comment = df.loc[df["num_comments"].idxmax()]
    print(f'Most commented story: "{top_comment["title"]}" — {top_comment["num_comments"]} comments')

# -----------------------------
# 3 — Add New Columns
# -----------------------------
def add_columns(df):
    avg_score = df["score"].mean()

    df["engagement"] = df["num_comments"] / (df["score"] + 1)
    df["is_popular"] = df["score"] > avg_score

    return df

# -----------------------------
# 4 — Save Result
# -----------------------------
def save_data(df):
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\nSaved to {OUTPUT_FILE}")

# -----------------------------
# MAIN
# -----------------------------
def main():
    df = load_data()
    numpy_analysis(df)
    df = add_columns(df)
    save_data(df)

if __name__ == "__main__":
    main()
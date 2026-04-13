import pandas as pd
import numpy as np

INPUT_FILE = "data/cleaned_trends.csv"
def load_data():
    df = pd.read_csv(INPUT_FILE)
    return df
def category_analysis(df):
    print("\n--- Category Counts ---")
    print(df["category"].value_counts())
def top_posts(df):
    print("\n--- Top 5 Posts by Score ---")
    top = df.sort_values(by="score", ascending=False).head(5)
    print(top[["title", "score", "category"]])
def numpy_analysis(df):
    scores = df["score"].values

    print("\n--- Score Statistics (NumPy) ---")
    print("Average score:", np.mean(scores))
    print("Max score:", np.max(scores))
    print("Min score:", np.min(scores))
def avg_score_per_category(df):
    print("\n--- Average Score per Category ---")
    print(df.groupby("category")["score"].mean())
def most_commented(df):
    print("\n--- Top 5 Most Commented Posts ---")
    top = df.sort_values(by="num_comments", ascending=False).head(5)
    print(top[["title", "num_comments", "category"]])
def main():
    print("Loading data...")
    df = load_data()

    category_analysis(df)
    top_posts(df)
    numpy_analysis(df)
    avg_score_per_category(df)
    most_commented(df)

    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
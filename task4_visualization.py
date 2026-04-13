import pandas as pd
import matplotlib.pyplot as plt
import os

INPUT_FILE = "data/trends_analysed.csv"
OUTPUT_DIR = "outputs"

# -----------------------------
# Setup
# -----------------------------
def setup():
    df = pd.read_csv(INPUT_FILE)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    return df

# -----------------------------
# Chart 1 — Top 10 Stories
# -----------------------------
def chart_top_stories(df):
    top = df.sort_values("score", ascending=False).head(10)

    # shorten titles
    titles = top["title"].apply(lambda x: x[:50])

    plt.figure(figsize=(10, 6))
    plt.barh(titles, top["score"])

    plt.title("Top 10 Stories by Score")
    plt.xlabel("Score")
    plt.ylabel("Title")

    plt.gca().invert_yaxis()

    plt.savefig(f"{OUTPUT_DIR}/chart1_top_stories.png")
    plt.show()

# -----------------------------
# Chart 2 — Category Counts
# -----------------------------
def chart_categories(df):
    counts = df["category"].value_counts()

    plt.figure(figsize=(8, 5))
    plt.bar(counts.index, counts.values)

    plt.title("Stories per Category")
    plt.xlabel("Category")
    plt.ylabel("Count")

    plt.savefig(f"{OUTPUT_DIR}/chart2_categories.png")
    plt.show()

# -----------------------------
# Chart 3 — Scatter Plot
# -----------------------------
def chart_scatter(df):
    popular = df[df["is_popular"] == True]
    not_popular = df[df["is_popular"] == False]

    plt.figure(figsize=(8, 5))

    plt.scatter(popular["score"], popular["num_comments"], label="Popular")
    plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

    plt.title("Score vs Comments")
    plt.xlabel("Score")
    plt.ylabel("Comments")
    plt.legend()

    plt.savefig(f"{OUTPUT_DIR}/chart3_scatter.png")
    plt.show()

# -----------------------------
# Dashboard (Bonus)
# -----------------------------
def dashboard(df):
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Chart 1
    top = df.sort_values("score", ascending=False).head(5)
    axes[0].barh(top["title"].str[:30], top["score"])
    axes[0].set_title("Top Stories")
    axes[0].invert_yaxis()

    # Chart 2
    counts = df["category"].value_counts()
    axes[1].bar(counts.index, counts.values)
    axes[1].set_title("Categories")

    # Chart 3
    axes[2].scatter(df["score"], df["num_comments"])
    axes[2].set_title("Score vs Comments")

    fig.suptitle("TrendPulse Dashboard")

    plt.tight_layout()

    plt.savefig(f"{OUTPUT_DIR}/dashboard.png")
    plt.show()

# -----------------------------
# Main
# -----------------------------
def main():
    df = setup()

    chart_top_stories(df)
    chart_categories(df)
    chart_scatter(df)
    dashboard(df)

    print("All charts saved in outputs/ folder")

if __name__ == "__main__":
    main()
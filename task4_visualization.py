import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "data/cleaned_trends.csv"
def load_data():
    df = pd.read_csv(INPUT_FILE)
    return df
def plot_category_counts(df):
    counts = df["category"].value_counts()

    plt.figure()
    counts.plot(kind="bar")

    plt.title("Number of Posts per Category")
    plt.xlabel("Category")
    plt.ylabel("Count")

    plt.savefig("data/category_counts.png")
    plt.show()
def plot_avg_score(df):
    avg_scores = df.groupby("category")["score"].mean()

    plt.figure()
    avg_scores.plot(kind="bar")

    plt.title("Average Score per Category")
    plt.xlabel("Category")
    plt.ylabel("Average Score")

    plt.savefig("data/avg_score.png")
    plt.show()
def plot_score_distribution(df):
    plt.figure()
    plt.hist(df["score"])

    plt.title("Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Frequency")

    plt.savefig("data/score_distribution.png")
    plt.show()
def main():
    print("Loading data...")
    df = load_data()

    print("Generating charts...")

    plot_category_counts(df)
    plot_avg_score(df)
    plot_score_distribution(df)

    print("Charts saved in data/ folder!")

if __name__ == "__main__":
    main()
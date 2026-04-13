# 📊 TrendPulse: What's Actually Trending Right Now

## 🚀 Project Overview

TrendPulse is a 4-stage data pipeline project that collects, processes, analyzes, and visualizes trending stories from Hacker News.

This project demonstrates skills in:

* API data collection
* Data cleaning using Pandas
* Data analysis using NumPy & Pandas
* Data visualization using Matplotlib

---

## 🧩 Project Structure

```
trendpulse-Kotha-Sumanth/
│
├── task1_data_collection.py      # Fetch data from HackerNews API
├── task2_data_cleaning.py        # Clean and convert JSON → CSV
├── task3_analysis.py             # Analyze data using NumPy & Pandas
├── task4_visualization.py        # Generate charts and graphs
│
└── data/
    ├── trends_YYYYMMDD.json      # Raw collected data
    ├── cleaned_trends.csv        # Cleaned dataset
    ├── category_counts.png       # Category distribution chart
    ├── avg_score.png             # Average score chart
    └── score_distribution.png    # Score histogram
```

---

## ⚙️ How It Works

### 🔹 Task 1: Data Collection

* Fetches top stories from Hacker News API
* Categorizes them into:

  * Technology
  * World News
  * Sports
  * Science
  * Entertainment
* Stores data in JSON format

---

### 🔹 Task 2: Data Cleaning

* Removes duplicate records
* Handles missing values
* Converts data types
* Saves cleaned data as CSV

---

### 🔹 Task 3: Data Analysis

* Category distribution
* Top 5 highest scored posts
* Most commented posts
* Statistical analysis using NumPy

---

### 🔹 Task 4: Visualization

* Bar chart: Number of posts per category
* Bar chart: Average score per category
* Histogram: Score distribution

---

## 📊 Key Insights

* Entertainment and Technology dominate trending content
* Some posts reach extremely high scores (2000+)
* Engagement varies significantly across categories

---

## 🛠️ Technologies Used

* Python
* Requests (API calls)
* Pandas (data processing)
* NumPy (analysis)
* Matplotlib (visualization)

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install requests pandas numpy matplotlib
```

### 2. Run tasks in order

```
python task1_data_collection.py
python task2_data_cleaning.py
python task3_analysis.py
python task4_visualization.py
```

---

## 📌 Output

* JSON dataset
* Cleaned CSV file
* Analysis results (console)
* Visualization charts (PNG)

---

## 🎯 Conclusion

TrendPulse provides a complete pipeline from raw API data to meaningful insights and visualizations, demonstrating real-world data processing skills.

---

## 👨‍💻 Author

**Kotha Sumanth**

---

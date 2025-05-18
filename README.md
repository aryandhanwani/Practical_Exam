# 🏃 Personal Fitness Data Tracker

This is a **command-line based Personal Fitness Data Tracker** developed in Python. The program allows users to log their fitness activities, analyze performance, visualize data, and generate reports using basic data science libraries like `pandas`, `matplotlib`, and `seaborn`.

---

## 📂 Project Features

1. **Log Fitness Activities**  
   - Add entries with `Activity Type`, `Duration (in minutes)`, and `Calories Burned`.
   - Automatically stores the current date.

2. **Data Loading & Cleaning**  
   - View first/last rows, handle missing values, and remove duplicates.

3. **Analysis & Metrics**  
   - Summarize total calories burned.
   - Show frequency and cumulative metrics by activity type.

4. **Data Filtering**  
   - Filter by activity name or date.
   - View mean, min, max, and total values for `duration` and `calories_burned`.

5. **Graph Generation**  
   - Bar chart: Activity vs Duration
   - Line plot: Calories Burned vs Duration
   - Pie chart: Percentage of duration by activity type
   - Heatmap: Correlation between `duration` and `calories_burned`

6. **Generate Report**  
   - Print statistical summary of your dataset.

---

## 🧰 Dependencies

Make sure you have the following Python libraries installed:

```bash
pip install pandas matplotlib seaborn
```

---

## 📁 Dataset

The application uses a CSV file `fitness_activities.csv` to store and read activity data. If this file does not exist, create it manually with the following columns:

```csv
date,activity_type,duration,calories_burned
```

You can leave it empty, the app will start populating it as you log activities.

---

## ▶️ How to Run

Simply run the script in your terminal or IDE:

```bash
python fitness_tracker.py
```

You'll be greeted with a menu interface allowing you to select various operations.

---

## 📝 Supported Activities

- Running  
- Yoga  
- Cycling  
- Strength Training  
- Swimming  
- Walking  

---

## 📊 Output Graphs

Saved visualizations include:
- `activity_duration_plot.png`
- `calories_duration_plot.png`
- `acitivty_duration_percentage.png`
- `calories_duration_heatmap.png`

---

## ⚠️ Notes

- Duration and Calories must be **positive integers**.
- Only supported activity types can be logged.
- Date format used is `YYYY-MM-DD`.

---

## ✅ Example Entry

```
Activity Type: Running
Duration: 30
Calories Burned: 250
```

Will be logged into the CSV file as:

```csv
2025-05-18,Running,30,250
```

---

## 🧑‍💻 Author

Developed as a beginner-friendly project to practice Python, data analysis, and visualization skills.

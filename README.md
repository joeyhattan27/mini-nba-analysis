# Mini NBA Analysis

A small exploratory data analysis (EDA) project on NBA player data using Python (Pandas, NumPy, and Matplotlib).

## Overview

This project analyzes NBA player statistics including age, height, weight, position, and salary. The goal is to practice data manipulation, filtering, aggregation, and basic visualization.

## Features

- Data cleaning: handle missing values, convert heights to inches, calculate derived columns (e.g., Salary in Millions, BigMan flag, IsYoungStar).
- Filtering and querying: select players based on age, salary, position, or team.
- Aggregation: compute averages and counts using `groupby`.
- Insights:
  - Average salary per team
  - Count of big men per team
  - Average age per position
  - Top 5 highest-paid players and youngest point guards
- Basic visualizations (optional, recommended):
  - Histograms, boxplots, scatter plots
  - Bar charts for team-level metrics

## Requirements

- Python 3.x
- Pandas
- NumPy
- Matplotlib (or Seaborn for enhanced visualizations)

## How to Run

1. Clone the repository.
2. Place `nba.csv` in the project folder.
3. Run `mini_nba_analysis.ipynb` or `mini_nba_analysis.py` in a Jupyter notebook or Python environment.
4. Inspect the output tables and visualizations.

## Notes

- Heights are converted from "feet-inches" format to total inches.
- `BigMan` is defined as players in positions "C" or "PF" taller than 6'9".
- `IsYoungStar` flags players under 25 years old with salary > $5M.

## Author

Joey Hattan

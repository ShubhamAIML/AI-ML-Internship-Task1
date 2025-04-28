# Data Cleaning & Preprocessing

## Overview
This repository contains the solution for Task 1 of the AI & ML Internship. The task focuses on learning data cleaning and preprocessing techniques using the Titanic Dataset. The goal was to handle missing values, explore the data, and visualize key features.

## Files
- `data_cleaning_with_graphs.py`: Python script used for data cleaning and visualization.
- `Titanic-Dataset.csv`: The original Titanic dataset with missing values.
- `cleaned_titanic_with_graphs.csv`: The cleaned dataset after handling missing values.
- `boxplot_age_fare.png`: Boxplot visualization of 'Age' and 'Fare' columns to explore data distribution.

## Steps Performed
1. **Data Exploration**:
   - Imported the Titanic dataset and printed basic info (data types, non-null counts) and missing value counts.
   - Identified missing values in `Age` (177), `Cabin` (687), and `Embarked` (2).

2. **Handling Missing Values**:
   - Filled missing `Age` values with the median and ensured no negative values using `clip(lower=0)`.
   - Filled missing `Embarked` values with the mode (most frequent value).
   - Dropped the `Cabin` column due to a high number of missing values (77% missing).

3. **Visualization**:
   - Created a boxplot for `Age` and `Fare` to visualize the data distribution and potential outliers.
   - Saved the boxplot as `boxplot_age_fare.png`.

4. **Saving Output**:
   - Saved the cleaned dataset as `cleaned_titanic_with_graphs.csv`.

## Tools Used
- Python
- Pandas (for data manipulation)
- Matplotlib/Seaborn (for visualization)

## How to Run
1. Install required libraries:
   ```bash
   pip install pandas matplotlib seaborn

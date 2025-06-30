# Data Exploration 📊🔍

This README provides a quick summary of the data exploration script for the
cleaned football transfer dataset.

📝 The script
[Transfer_Dataset_Data_Exploration.ipynb](Transfer_Dataset_Data_Exploration.ipynb)
performs an initial exploratory data analysis (EDA) on the
"Transfer_Dataset.cleaned.csv" dataset.

The goal is to
understand the structure, content, and key characteristics of the football player
transfer data.

## ⚽ Dataset Explored

Dataset Name: Transfer_Dataset.cleaned.csv (data loaded from Transfer_Dataset.raw.csv)

Content: Contains information about football player transfers, including player
names, transfer fees, seasons, source and destination clubs/leagues, and player positions.

## 🔍 How it Explores the Data

The script follows a standard EDA workflow:

📥 Loading Data:

Loads the dataset into a pandas DataFrame.

👀 Initial Data Look:

Displays the first 5 rows (df.head()).

Displays the last 5 rows (df.tail()).

Shows 5 random rows (df.sample(5)).

Checks the dimensions (rows, columns) of the DataFrame (df.shape).

Provides metadata about the DataFrame, including column data types and non-null
counts (df.info()).

Lists all column names (df.columns).

## 🧹 Missing Values & Duplicates

Checks for and sums any missing values across all columns (df.isnull().sum()).

Checks for and sums any duplicate rows (df.duplicated().sum()).

## 📈 Statistical Summary

Generates a statistical summary for all columns, including count, unique values,
top occurring value, and frequency for object types, and mean, std, min, max, and
quartiles for numerical types (df.describe(include="all")).

Provides a detailed statistical summary specifically for the 'Transfer Fee'
numerical column (df["Transfer Fee"].describe()).

## 📊 Data Visualization

💰 Top 10 Most Expensive Transfers: Visualizes the top 10 transfers by fee
using a bar plot.

🗓️ Total Transfer Spending by Season: Shows the trend of total transfer
spending over different seasons using a line plot.

🥅 Number of Transfers by Position: Displays the distribution of transfers
across different player positions using a count plot.

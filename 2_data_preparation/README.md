# Data Cleaning & Preparation Script 🧹✨

This README provides a quick summary of the data Preparation script for the
("Transfer_Dataset.raw.csv") dataset.

The script [Transfer_Dataset_Data_Preparation.ipynb](Transfer_Dataset_Data_Preparation.ipynb)
is designed to clean and preprocess the raw
football transfer dataset.

**Input Dataset:** Transfer_Dataset.raw.csv 📥
This is the primary raw dataset containing information about football player
transfers.⚽

**Processing Steps 🛠️**
The script performs the following data cleaning and preparation steps:

1) Load Data: Reads the Transfer_Dataset.raw.csv file into a Pandas DataFrame. 📂

2) Filter by Season: Excludes all transfer entries that occurred before the
'2018/2019' season. 🗓️

3) Handle Missing Null Values 🗑️

4) Identifies and replaces string representations of missing values (e.g., "-")
with NaN (Not a Number). 🚫

5) Removes any rows that contain NaN values across all columns. ✂️

6) Fix Data Types: Converts the 'Transfer Fee' column from an object (string) type
to a numerical (float64) type, coercing any non-numeric values to NaN 🔢

**Output Dataset:** Transfer_Dataset.cleaned.csv ✅
This file contains the cleaned and preprocessed data, with only transfers from
2018/2019 onwards, no missing values, and the 'Transfer Fee' as a numerical
column. 📈

*This output dataset is saved to the /1_datasets directory. 📁

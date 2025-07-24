# Data Cleaning & Preparation Scripts ⚽📊🧹✨

This README describes the two key scripts used to clean and prepare raw football
datasets for analysis. The goal is to transform messy, unstructured data into
well organized, clean formats ready for comparing player performance before and
after transfers.

---

## Section 1: Transfer Dataset Cleaning 📁📉

This section explains the preparation process for the [`transfer_dataset.raw.csv`](../1_datasets/raw/transfer_dataset.raw.csv)
file.

The script [`transfer_dataset_data_preparation.ipynb`](./transfer_dataset_data_preparation.ipynb)
cleans and prepares this raw transfer dataset for analysis.

### 🔹 Input Dataset

**File:** [`transfer_dataset.raw.csv`](
../1_datasets/raw/transfer_dataset.raw.csv) 📥
This is the primary raw dataset containing information about football player transfers.⚽

### 🔧 Processing Steps

1. **Load Data:**  
   - Reads the [`transfer_dataset.raw.csv`](../1_datasets/raw/transfer_dataset.raw.csv)
   file into a Pandas DataFrame. 📂

2. **Filter by Season:**  
   - Excludes all transfer entries that occurred before the '2018/2019' season. 🗓️

3. **Handle Null Values:**  
   - Replaces string placeholders like "-" with `NaN`. 🚫  
   - Removes rows with missing values. ✂️

4. **Fix Data Types:**  
   - Converts 'Transfer Fee' from string to numeric (float64). 🔢  
   - Non-numeric values are coerced to NaN.

### ✅ Output Dataset

**File:** [`transfer_dataset.cleaned.csv`](../1_datasets/cleaned/transfer_dataset.cleaned.csv)

- Only includes transfers from 2018/2019 onward  
- No missing values  
- 'Transfer Fee' is a numeric column  
- Saved to the `/1_datasets` directory 📁

---

## Section 2: Player Statistics Dataset Cleaning 📊📂

This sections explains the process of cleaning and preparing raw football player
statistics to make them ready for analysis, especially for understanding how
performance changes before and after transfers.

---

### 🎯 Context

Imagine having player performance stats across. This section describes how we
convert such raw
stats into clean data for **pre-transfer** and **post-transfer** analysis.

---

### Why Clean the Data❓

Raw stats often contain missing values, bad formatting, and inconsistencies.
Cleaning helps avoid analysis errors and ensures all data is reliable and
structured.

---

### 📁 Input Data

We start with:

- **Multiple raw CSVs:** Stats from each season and transfer window  
  (e.g., [`2018-19_Transfers_2016-17_to_2019-20_Stats.raw.csv`](
    ../1_datasets/raw/2018-19_Transfers_2016-17_to_2019-20_Stats.raw.csv))  
- **One cleaned transfer dataset:** [`2018-19_Transfers_2016-17_to_2019-20_Stats.raw_cleaned_common.csv`](../1_datasets/cleaned/2018-19_Transfers_2016-17_to_2019-20_Stats.raw_cleaned_common.csv)
(with player positions)

---

### 🧼 Step-by-Step Cleaning Process

#### 🔹 Step 1: Clean Individual Season Files

- **Drop % Columns:** Remove columns that contain '%' (e.g., "Pass Completion %")
- **Extract Player Names:** From embedded URLs to a clear "Player Name" column
- **Fix Numbers:**  
  - Remove commas from values (e.g., "1,000" → 1000)  
  - Convert string-based numerics to numeric types (int and/or float) 🔢
- **Fill Missing Values:**  
  - **Filling with 0:** For certain statistics like `"Penalties conceded"`,  
    `"Penalties awarded"`, and `"Red cards"`, a missing value typically means  
    the event **did not occur** for that player. So, it makes logical sense to  
    fill in a zero (0️⃣) to represent absence of the event.  
    For example, if a player has no recorded red cards, it's usually because  
    they didn’t receive any, not because data is unavailable.
  
  - **Filling with Median:** For other numerical columns like `"Passes completed"`,
    `"Tackles"`, or `"Interceptions"`, a missing value could mean incomplete  
    data due to data entry errors, scraping issues, or lack of tracking.  
    Instead of dropping these rows, we impute with the **median** of the column.
    The median is less affected by outliers and gives a balanced replacement  
    that won't skew analysis as much as a mean would. 📊

Each cleaned season file is saved as `*_cleaned_common.csv` ✅

#### 🔹 Step 2: Find Common Columns Across Seasons

- Identify columns that appear in **every** cleaned season file 🧩  
- Filter all files to keep only these shared columns  
- Re-save them for consistency across datasets 💾

#### 🔹 Step 3: Create "Before" and "After" Datasets

- For each player:
  - Split data into **before** and **after** their transfer year 🗓️  
  - Average stats across each period ➕➗  

#### 🔹 Step 4: Merge with Position Info

- Load position data from [`transfer_dataset.cleaned.csv`](../1_datasets/cleaned/transfer_dataset.cleaned.csv)
- Map detailed positions into general roles:
  - "Attack", "Midfield", "Defense" 🥅⚽🛡️  
- Merge position info using "Player Name" column 🔗  

- **Handle Missing Position Values:**  
  After comparing the `player stats` with the [`cleaned transfer dataset`](../1_datasets/cleaned/transfer_dataset.cleaned.csv),
  which contains detailed position information, and assigning positions accordingly,
  some players still had **missing values** in the position column.

  This occurred mainly due **mismatches in player names** between the two  
  datasets. These mismatches were caused by:

- Differences in name formatting (e.g., "é" vs "e", or inclusion of middle names)
- Cleaning steps that stripped or altered characters  
- Inconsistencies in how names were scraped from different sources

  As a result, some names in the player stats didn’t match exactly with the names
  in the transfer dataset, causing the empty values for those cells.

  **Why we fixed them manually:**  

- The dataset was relatively small  
- Due to limited time, implementing and testing a fuzzy matching solution or  
    rewriting the cleaning logic to handle all name variations would have taken
    longer  
- Manual review and entry was faster and ensured no critical data was lost

  Each missing entry was manually reviewed and assigned a general role  
  ("Attack", "Midfield", or "Defense") to ensure complete and  
  consistent datasets for analysis. 📝

- Saved as:
  - [`pre_transfer_cleaned.csv`](
    ../1_datasets//cleaned/pre_transfer_cleaned.csv) ⬅️
  - [`post_transfer_cleaned.csv`](
    ../1_datasets/cleaned/post_transfer_cleaned.csv) ➡️

---

### 🎉 Final Outputs

You will get the following cleaned datasets:

- `*_cleaned_common.csv` – Cleaned season stats with shared columns ✨
  - For example:  [`2018-19_Transfers_2016-17_to_2019-20_Stats.raw_cleaned_common.csv`](../1_datasets/cleaned/2018-19_Transfers_2016-17_to_2019-20_Stats.raw_cleaned_common.csv)
- [`pre_transfer_cleaned.csv`](../1_datasets/cleaned/pre_transfer_cleaned.csv)
– Stats before player transfers ⬅️  
- [`post_transfer_cleaned.csv`](../1_datasets/cleaned/post_transfer_cleaned.csv)
– Stats after player transfers ➡️  

These final datasets are ready for visualizations, modeling, and statistical
analysis on how transfers affect player performance 🚀📈

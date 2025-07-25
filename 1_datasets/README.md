# ⚽ Player Transfers & Performance - Dataset Documentation

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](../LICENSE)
![Made With ❤️](https://img.shields.io/badge/Made%20with-Love-orange.svg)
![Dataset Status](https://img.shields.io/badge/Datasets-Up%20to%20Date-brightgreen.svg)

Welcome! 👋 This folder contains the raw and processed datasets used in our
research project about player performance after transferring from lower-tier
football leagues to a top-tier league.

---

## 🧠 Research Goal

> **Which individual attributes—like height, pace, age, or previous league
experience—most strongly predict a football player’s successful performance
after transferring from a lower-tier league (e.g.
Eredivisie) to a top-tier league (e.g., Premier League)?**

Since there’s no ready-made dataset for this specific question, we created our
own by scraping from trusted sources.

> ⚠️ **Note:**  
>
> - We are **excluding goalkeepers** to keep the analysis focused and because
more consistent data is available for outfield players (defenders, midfielders, forwards).
> - We are also **excluding loaned players** after their transfer, since their
playing time and role in the club are often unclear or temporary. This helps us
focus on **full-time transfers** and get more reliable post-transfer performance
metrics.

---

## 🛠️ Data Collection Sources

### 🔄 1. [Transfer Data (Transfermarkt)](https://www.transfermarkt.com)

We scraped player transfer data from **2014–2023** for those who moved from
lower-tier leagues to the **English Premier League**.

- 📄 [`transfer_dataset.raw.csv`](../1_datasets/raw/transfer_dataset.raw.csv)  
  *Raw list of transfers with player name, origin league, destination club,
  transfer fee, etc.*

## 📊 2. [Player Stats (Fotmob)](https://www.fotmob.com)

We gathered **performance metrics and attributes** for each player in our
transfer list from Fotmob, covering seasons **before and after** their transfer
(where available).

These stats include things like appearances, goals, assists, pass completion
rate, defensive contributions, and more.

Since there was no ready-made dataset for these performance metrics, the data
was manually scraped from Fotmob pages for each player.

Additionally, we included **each player's average rating**, which was **manually
entered** using data from [Sofascore](https://www.sofascore.com/).  
This step was done manually because Sofascore’s HTML/CSS structure made automated
scraping difficult and time-consuming.

To speed things up, this manual data entry was divided among team members.  
Since the dataset wasn't very large, this was a practical solution.

---

## 🧪 Raw vs. Cleaned Stats: A Quick Preview

Here’s a simplified comparison of raw vs. cleaned player stats data:

| URL                    |Season|Average Rating|Defending - Aerial duels won|
|------------------------------------------------------|-------------------|--------|--------------|
| <https://www.fotmob.com/players/603537/angelino>                              | 2017/18            | 7.21 | 0.38         |
| <https://www.fotmob.com/players/408943/takumi-minamino>                             | 2017/18             | 6.82 |       |

⬇️ After cleaning:

| Player Name  | Season | Average Rating | Defending - Aerial duels won |
|--------------|------------------|------------|-------------------|
| Angelino   | 2017/18            | 7.21       | 0.38              |
| Takumi Minamino  | 2017/18            | 6.82       | 1.34               |

## 🧼 Dataset Usage

We’re using this data to:

- Compare each player's **before vs. after** performance.
- Label players as **"successful"** or **"unsuccessful"** based on:
  - Minutes played
  - Ratings relative to others in the same position (defender, midfielder, forward)
- Use those labels to identify which **attributes**
(like age, height, pace, specific metrics)
are common in **successful players**.
- Create a model that can **predict the success** of future transfers from
lower-tier leagues.

> ⚠️ Of course, no dataset or model can fully predict a player's future
success—but this narrows down the scouting pool and adds data-driven support to recruitment.

---

## 🧹 Cleaned & Aggregated Datasets

After the raw stats files are cleaned and aligned across seasons, we create
**two final performance datasets**:

- **[`pre_transfer.cleaned.csv`](../1_datasets/cleaned/pre_transfer.cleaned.csv)**  
  Average performance metrics **before** a player's transfer to the Premier
  League.

- **[`post_transfer.cleaned.csv`](../1_datasets/cleaned/post_transfer.cleaned.csv)**  
  Average performance metrics **after** the transfer.

- **[`transfer_dataset.cleaned.csv`](../1_datasets/cleaned/transfer_dataset.cleaned.csv)**  
   Contains the cleaned metadata of player transfers, including name, position,
   transfer fee, and club info.

These datasets are saved in the [`/1_datasets/cleaned/`](../1_datasets/cleaned/)
folder and are used to:

- Analyze how individual metrics change after a player transfers
- Label players as **"successful"** or **"unsuccessful"**
- Train machine learning models to predict future transfer success

Each record in these (`pre/post transfer`) datasets represents **a unique player**,
with numeric
performance averages computed over multiple seasons (`pre/post transfer`) where data
is available.

---

### 📊 Sample of Pre-Transfer Dataset

Below is a preview of the aggregated player statistics **before** their transfers.
This data is grouped by player name and averaged across all pre-transfer seasons.

| Player Name| Average Rating | Defending - Aerial duels won | Defending - Blocked|
|-----------------|-------------|---------|-------|
| Aaron Lennon      | 6.58        | 0.2    | 0.26  |
| Aaron Mooy   | 6.99        | 0.77    | 0.49   |
| Adam Armstrong   | 7        | 0.32    | 1.09 |

> ℹ️ The **post-transfer dataset** follows a **similar format**, with player  
> statistics aggregated for seasons **after** the transfer.

---

## 🧾 File Naming Convention

- All **raw datasets** are saved as `*.raw.*` to indicate they’re **untouched
from source**.
  - For example, the raw stats files are named like this:  
[`2019-20_Transfers_2017-18_to_2020-21_Stats.raw.csv`](
  ../1_datasets/raw/2019-20_Transfers_2017-18_to_2020-21_Stats.raw.csv)
This means the player was transferred in the **2019–20 season**, and the file  
contains their stats for the **seasons from 2017–18 to 2021–22**.
- Any **cleaned or processed versions** are saved separately with **descriptive names**.
Like this:  
[`post_transfer.cleaned.csv`](../1_datasets/cleaned/post_transfer.cleaned.csv)

---

## 🧠 Data Types & Categories

Here are the different ways we think about and organize the datasets:

- **By Data Type**: numerical (height, pace), categorical (position, league)
- **By Structure**: tabular
- **By Collection Method**: manually scraped
- **By Format**: `.csv`
- **By Purpose**: raw, cleaned, modeling-ready
- **By Access Type**: public data, no login required

---

## 📁 Folder Guidelines

If you’re contributing or using this repo:

- Do **not overwrite** raw datasets.
- When cleaning data, always save the result as a **new file** with a
descriptive name.
- Document new datasets here in the README as you go.

---

## 💡 Want to Help?

We're always open to feedback, contributions, and suggestions—feel free to open
an [issue](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-23-repo/issues)
or submit a PR!

---

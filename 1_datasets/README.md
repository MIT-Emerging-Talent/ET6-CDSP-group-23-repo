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
> ⚠️ **Note:** We are **excluding goalkeepers** from this research to keep the
analysis more focused and because richer, more consistent data is available for
outfield players (defenders, midfielders, forwards).

---

## 🛠️ Data Collection Sources

### 🔄 1. [Transfer Data (Transfermarkt)](https://www.transfermarkt.com)

We scraped player transfer data from **2014–2023** for those who moved from
lower-tier leagues to the **English Premier League**.

- 📄 [`transfers_2014_2023.raw.csv`](./transfers_2014_2023.raw.csv)  
  *Raw list of transfers with player name, origin league, destination club,
  transfer fee, etc.*

### 📊 2. [Player Stats (Fotmob)](https://www.fotmob.com)

We then gathered **performance metrics and attributes** of the players in our
transfer list from Fotmob, both **before and after** the transfer (when available).

- 📄 [`player_attributes_fotmob.raw.json`](./player_attributes_fotmob.raw.json)
  *Includes height, country, pass accuracy, goals, etc.*

---

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

## 🧾 File Naming Convention

- All **raw datasets** are saved as `*.raw.*` to indicate they’re **untouched
from source**.
- Any **cleaned or processed versions** are saved separately with **descriptive names**.

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
- Document new datasets here in the README as you go!

---

## 💡 Want to Help?

We're always open to feedback, contributions, and suggestions—feel free to open
an [issue](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-23-repo/issues)
or submit a PR!

---

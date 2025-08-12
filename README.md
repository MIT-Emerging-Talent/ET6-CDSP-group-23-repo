# Data Strikers ⚽🏆

Welcome to **Data Strikers** , a collaborative research initiative that explores
football through the lens of data science. Our mission is to build reproducible,
insight‑rich projects that illuminate how the beautiful game really works—from
the factors behind an individual’s scoring prowess to the subtle dynamics of
match officiating and injury risk. This repository collects our code, data
workflows, and findings so that students, practitioners, and fans can learn
from—and build upon—our work.

---

## 📋 Project Milestones

## ✅ Half-Time Report: Milestones Conquered

### Milestone 0: The Kick-Off - Cross-Cultural Collaboration!🌍🤝

Our journey began by uniting as the Data Strikers! This foundational milestone
was all about getting to know each other, agreeing on our collaboration and
communication rules, and defining our project's initial constraints.

*Check out our [collaboration](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-23-repo/tree/main/collaboration)
framework*

### Milestone 1: Scouting for Gold - Problem Identification 🔍

And so our Mission Begins!

In this phase, we took a deep dive into the world of football transfers, exploring
potential research directions through dynamic team discussions and critical thinking.
After thoughtful analysis and collaboration, we locked in a focused, high impact
research question — the foundation of our entire project!

Want to see how our ideas evolved? Check out our brainstorming journey in the
[Brainstorming Document](https://docs.google.com/document/d/1GjkHdTqSOaXvgHSFjAw1yVrvjhfK8PqvNB8PJSDNICs/edit?usp=sharing),
 and explore the final output that shaped our direction in the milestone
[Domain Study folder](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-23-repo/tree/main/0_domain_study).

### 📌 Problem Statement

In the highly competitive and financially driven world of professional football,
clubs often invest heavily in players transitioning from lower-tier leagues to
top-tier leagues. However, there's a significant degree of uncertainty regarding
whether these players will successfully adapt and perform at the higher level.
This lack of predictive insight can lead to suboptimal transfer decisions, wasted
resources, and underperforming squads. Our project seeks to address this challenge
by providing a data-driven framework to identify the key individual attributes
that are most indicative of a player's successful adaptation and performance in
a more demanding league environment.

### 🎯 Our Million-Dollar Actionable Research Question

**Which performance metrics from players in lower-tier football leagues are the
strongest predictors of success in the Premier League, and how do these key
indicators vary by player position (defenders, midfielders, and attackers)?**

### Milestone 2: Filling the Trophy Cabinet - Data Collection📊

This milestone was divided into 3 stages, Data Collection, Data Preperation and
Data Exploration.

#### 1️⃣ Data Collection 📥

In this stage, We gathered two essential datasets:  

- A **Transfer Dataset** detailing player moves between leagues.  
- A **Player Stats Dataset** containing individual attributes like pace, age,
and more.  

📁 All raw datasets and accompanying documentation are available here:  
🔗 [Datasets folder](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-23-repo/tree/main/1_datasets)

#### 2️⃣ Data Preparation 🛠️

With the raw data in hand, it was time to clean, standardize, and get it ready
for analysis.  

- We handled missing values, renamed columns, filtered players, and merged
relevant info.  

The data preparation script and a step-by-step guide are available here:  
🔗 [Data Preparation folder](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-23-repo/tree/main/2_data_preparation)

#### 3️⃣ Data Exploration 🔍

Finally, we dove into the cleaned datasets to uncover patterns, distributions,
and early insights.  

- This helped us better understand the landscape of successful transfers.  

Our exploration methods and notebooks can be found here:  
🔗 [Data Exploration folder](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-23-repo/tree/main/3_data_exploration)

### Milestone 3: Breaking Down the Opposition - Data Analysis📈

In this milestone, we tackled our core research question by building predictive
models to identify which player attributes from lower-tier leagues are the
strongest indicators of success in the Premier League.

We analyzed 149 player transfers into the Premier League, building Random Forest
models separately for attackers, midfielders, and defenders to reflect the unique
traits needed for success
in each role.

### 🧠 Modeling Approach

We defined “success” as:

Average Rating ≥ 6.7

1000+ Minutes Played over 2 Seasons

### 📊 Key Findings

- Attackers were the most predictable, with **83%** accuracy. Interestingly, chances
created and accurate crosses were more important than goals scored.

- Midfielders and Defenders were less predictable, both around **62%** accuracy.

- For midfielders, ball touches and pass success were key.

- For defenders, surprisingly, goals scored and shots taken were more predictive
than traditional defensive metrics, highlighting a shift towards more versatile,
attack-minded players.

Overall, our findings suggest that modern football values technical versatility
across all positions.

For a deeper dive into the technical details of our models, check out the
🔗 [Technical Report](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-23-repo/tree/main/4_data_analysis/technical_report.md)
and the 🔗 [rf_models_summary.md](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-23-repo/tree/main/4_data_analysis/rf_models_summary.md).

You can also find a more detailed non-technical overview of our findings in
🔗 [Non Technical Report](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-23-repo/tree/main/4_data_analysis/non_technical_report.md).

For a deep dive into the full analysis and visuals, check the
🔗 [Data Analysis folder](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-23-repo/tree/data_analysis_doc/4_data_analysis).

### Milestone 4: Celebrating the Win - Communicating Results📣

With our key insights in hand, it was time to share them with the world!
In this milestone, we identified and analyzed our target audience, from football
fans to journalists and scouting agents, and explored the best ways to reach them.
Our findings and approach are detailed in this
🔗 Target Audience Document.

To make our work accessible to everyone, we also built a website that brings our
results to life in a clear and engaging way. Check it out here: 🔗[Data Strikers
website!](<https://datastrikers.netlify.app/>)

## ⏳ The Second Half: Milestones Awaiting

### Milestone 5: The Grand Final - Final Presentation🏆

---

## 🗺️ Our Stadium Map

<pre>
README.md                     # You're reading it now!
├── 0_domain_study/           # Initial domain research and brainstorming
├── 1_datasets/               # Raw and processed data
├── 2_data_preparation/       # Scripts for data cleaning/preprocessing
├── 3_data_exploration/       # Notebooks for initial analysis
├── 4_data_analysis/          # Advanced modeling and insights
├── 5_communication_strategy/ # Plan for sharing results
├── 6_final_presentation/     # Final deliverables/presentation
├── collaboration/            # Team working/collaboration documents
├── notes/                    # Learnings and meeting notes
└── requirements.txt          # Required project dependencies
</pre>
---

## ⭐Meet the Data Strikers⭐

| Team Member   | GitHub    |Fav Football team  |
| :-------------- | :----------------------- | :------------------- |
|  Abdul Qader Dost |  [@abeddost](https://github.com/abeddost) | Real Madrid ⚪👑   |
| Hamidullah Rajabi | [@hamid4231](https://github.com/hamid4231)   |  Real Madrid ⚪👑  |
| Khusro Sakhi| [@Khusro-S](https://github.com/Khusro-S)  |  Real Madrid ⚪👑 |
| Saeed Emad |[@Saeed-Emad](https://github.com/Saeed-Emad)   |     FC Barcelona 🔵🔴       |
| Tibyan Bilal | [@TibyanKhalid](https://github.com/TibyanKhalid)    | FC Barcelona 🔵🔴   |
| Arthur Dorvil | [@Mr-Glucose](https://github.com/Mr-Glucose)    |    |

## ⚙️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📜License

All code is released under the MIT License. Data files remain under the terms
specified by their original providers.

---

*For questions or collaboration proposals, open an issue or reach out to any
member of **Data Strikers**.*

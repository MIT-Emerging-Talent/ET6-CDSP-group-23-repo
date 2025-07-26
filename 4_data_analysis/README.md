
# ⚽ Predicting Premier League Success — Data Analysis

This folder contains the core predictive modeling work behind our research question:

> **"Which individual attributes — such as height, pace, age, or previous league
> experience — most strongly predict a player's successful performance after
> moving from a lower-tier league (e.g., Eredivisie) to a top-tier
> league (e.g., Premier League)?"**

We framed this as a **binary classification problem**, where success is defined as:

- **Average Rating ≥ 6.7**
- **Total Minutes Played ≥ 1000 over two seasons**

---

## 📂 Folder Purpose

The notebooks in this folder:

1. **Read cleaned datasets** from the `0_datasets/` folder.
2. **Train predictive models** (Random Forest classifiers) separately for
   attackers, midfielders, and defenders.
3. **Visualize performance**, including:
   - Feature importance bar charts
   - Confusion matrix plots
4. Output performance metrics like accuracy and ROC-AUC.

---

## 📁 Notebooks & Scripts

| File                                 | Purpose                                |
|--------------------------------------|----------------------------------------|
| `labeling_data.ipynb`                | Add success/failure labels             |
| `rf_predicting_transfer_attackers.ipynb` | Random Forest model for attackers  |
| `rf_predicting_transfer_midfielders.ipynb` | Random Forest for midfielders    |
| `rf_predicting_transfer_defenders.ipynb` | Random Forest for defenders        |
| `rf_models_summary.md`               | Summary of models and results          |
| `technical_report.md`                | Detailed technical project report      |
| `non_technical_report.md`            | Plain-language summary and insights    |

---

## 🔬 Analysis Strategy

### 📌 Position-Specific Modeling

We built **separate models per player position group**:

- **Attackers** (e.g., strikers, wingers)
- **Midfielders** (central, attacking, defensive)
- **Defenders** (center-backs, full-backs)

This allowed for customized feature selection and insights tailored to each
role's requirements in the Premier League.

### 🧠 Why We Chose Random Forest

Random Forest classifiers were selected due to:

- High interpretability (feature importance)
- Robust performance on small and unbalanced datasets
- Ability to handle non-linear relationships and missing data

We compared Random Forest with Logistic Regression and Gradient Boosting but
prioritized simplicity, generalization, and transparency.

---

## 📊 Key Insights

- **Attackers** are the most predictable (83% accuracy), with creativity
  (chances created, successful crosses) being more important than goal-scoring alone.
- **Midfielders** are harder to predict — touches and pass involvement are
   helpful, but model accuracy was lower (62%).
- **Defenders** showed surprising trends: offensive stats like goals and shots
   were more predictive than tackles or blocks.
- Small test sizes (13–17 players per group) limit generalizability.
- Modern football increasingly rewards **technical versatility** across all positions.

---

## 📈 Visual Output Included

The following visuals are generated and saved in the `figures/` directory and
referenced in our Non-Technical Report:

- **Feature Importance Charts**  
  Help us understand which variables mattered most in model decisions.
- **Confusion Matrices**  
  Give us a clear picture of how many predictions were correct vs. incorrect.

---

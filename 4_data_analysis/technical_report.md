# ⚽ Technical Analysis: Predicting Premier League Success

## 🎯 Objective

This project aimed to predict which football players would succeed after
 transferring from lower-tier leagues to the Premier League. We framed this as a
  **binary classification problem**:  
> “Will this player succeed or not?”

**Success Criteria:**

- Average Rating ≥ 6.7
- At least 1000 minutes played across 2 seasons

---

## 📊 Dataset Overview

- **Total Players:** 149  
- **By Position:** Attackers (50), Midfielders (43), Defenders (56)  
- **Data Split:** 70% training, 30% testing  
- **Test Sets:** 15 attackers, 13 midfielders, 17 defenders

---

## 🌲 Why Random Forest?

### 🔎 What It Is

A Random Forest is an ensemble of decision trees. It combines their predictions
 to reduce overfitting and improve generalization.

### ✅ Why We Chose It

- **Handles Nonlinear Relationships** well  
- **Robust to Missing Values**  
- **Provides Feature Importance** – helps us interpret model output  
- **Low Overfitting Risk** – generalizes better than single trees

### 🔄 Alternatives Considered

#### Logistic Regression

- ✅ Interpretable coefficients  
- ✅ Suitable for small datasets  
- ❌ May miss complex patterns

#### Gradient Boosting (XGBoost / LightGBM)

- ✅ Often more accurate  
- ❌ Sensitive to hyperparameters  
- ❌ Higher overfitting risk on small data

---

## 🧪 Methodology

### 🔍 Feature Selection

We selected features based on football domain knowledge:

- **Attackers:** Goals, assists, key passes, crosses, shot accuracy  
- **Midfielders:** Passes, dribbles, touches, tackles  
- **Defenders:** Tackles, clearances, goals (!)

### 🏗️ Model Training

Trained Random Forest classifiers for each position using 70% of data.

### 🧪 Model Evaluation

Tested on the remaining 30%, using Accuracy and ROC-AUC.

---

## 📈 Results & Interpretation

### 🔢 Performance Metrics

| Position    | Accuracy | ROC-AUC |
|-------------|----------|---------|
| Attackers   | 83%      | 0.83    |
| Midfielders | 62%      | 0.62    |
| Defenders   | 62%      | 0.62    |

> **ROC-AUC** = Model’s ability to rank players from most to least likely  
> to succeed.  
> 0.5 = random guessing, 1.0 = perfect.

### 🧠 Key Insights

- Attacking success is **most predictable**
- **Chance creation > pure scoring** for attackers
- **Midfield and defense harder to model** – likely due to non-statistical factors
- **Versatile defenders** outperform others

---

## ⚠️ Limitations

### 1. Small Test Sets

- Only ~15 players per position
- A few errors skew results significantly

### 2. No Cross-Validation

- One-time test split
- No robustness check

### 3. Class Imbalance

- Likely more failures than successes
- Models may favor predicting "fail"

---

## 🔄 What Could Be Done Better

### 🔧 Feature Engineering

Instead of basic stats, engineer smarter metrics:

- `Goals per shot` or `xG per 90`  
- `Progressive passes per 90` or `Passes into final third`

### ✅ Better Validation

- K-Fold Cross-Validation  
- Bootstrap sampling  
- Time-based data splits (train on older, test on recent)

### 🧱 Sub-Position Modeling

Split roles further:

- Defenders → CB, FB  
- Midfielders → DM, CM, AM  
- Attackers → ST, Winger

---

## 💡 Alternative Modeling Ideas

### 🔗 Ensemble Learning

```python
from sklearn.ensemble import VotingClassifier
VotingClassifier([
    ('lr', LogisticRegression()),
    ('rf', RandomForestClassifier()),
    ('svc', SVC())
])

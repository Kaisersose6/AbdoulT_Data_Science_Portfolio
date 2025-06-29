# Credit Default Prediction

This project uses the UCI "Default of Credit Card Clients" dataset to predict whether a credit card holder will default on their payment next month.

## 📊 Dataset
- **Source**: [Kaggle](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset)
- 30,000 observations with 23 features, including payment history, credit limit, and demographics.

## 🧠 Models
- Logistic Regression (baseline)
- XGBoost (tuned)

## ⚙️ Techniques
- Feature Engineering (e.g., payment ratios, WOE binning)
- Class Imbalance Handling (SMOTE)
- Model Evaluation: AUC-ROC, Precision, Recall
- SHAP for Interpretability

## 📁 Folder Structure
- `data/`: Raw dataset
- `notebooks/`: Jupyter notebooks (EDA, modeling, SHAP)
- `scripts/`: Python scripts for pipeline automation
- `outputs/`: Final model metrics, SHAP plots

## 🚀 Results
- Best Model: XGBoost (AUC: 0.80, Precision: 0.70)
- Key Drivers: Past payment history, utilization, and limit balance

## 🛠️ Tech Stack
Python, Pandas, scikit-learn, XGBoost, SHAP, Matplotlib


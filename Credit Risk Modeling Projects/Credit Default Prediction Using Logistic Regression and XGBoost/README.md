# Credit Default Prediction

**Domain:** Financial risk · Credit scoring · **Stack:** Python · Logistic Regression · XGBoost · SHAP

---

## Overview

I built this project to demonstrate end-to-end binary classification for credit risk — from raw loan application data through feature engineering, model comparison, SHAP explainability, and probability calibration. Predicting default probability is one of the highest-stakes ML applications in financial services, and this project treats explainability as a first-class requirement, not an afterthought.

The methodology reflects work I contributed at Wells Fargo, where I applied statistical modeling to improve fraud pattern detection and reduce analytical errors across regulatory data pipelines.

---

## Business problem

A well-calibrated credit default model enables three things a lender cannot do well without one:

1. **Risk-based pricing** — charge rates that reflect actual default probability per applicant
2. 2. **Proactive intervention** — identify at-risk accounts early enough to offer hardship programs
   3. 3. **Regulatory compliance** — document model decisions with auditable feature-level explanations (SR 11-7)
     
      4. ---
     
      5. ## Data
     
      6. - Source: Home Credit Default Risk (publicly available via Kaggle)
         - - ~300,000 loan applications with repayment outcomes
           - - Features: bureau credit history, income, employment status, loan characteristics, payment behavior
             - - Target: binary (1 = default within 12 months, 0 = no default)
               - - Class imbalance: ~8% positive rate, handled via SMOTE and threshold optimization
                
                 - ---

                 ## Technical approach

                 ### Feature engineering
                 - Bureau aggregations: max delinquency, total past loans, credit utilization ratio
                 - - Payment behavior features: rolling late payment counts, days past due averages
                   - - Application ratios: annuity-to-income, credit amount-to-income
                     - - Target encoding for high-cardinality categoricals with cross-validation to prevent leakage
                      
                       - ### Modeling pipeline
                       - Three models trained and evaluated on identical train/validation splits:
                      
                       - | Model | ROC-AUC | KS Statistic | Precision@top 10% |
                       - |---|---|---|---|
                       - | Logistic Regression (L2) | 0.74 | 0.38 | 0.41 |
                       - | Random Forest | 0.77 | 0.43 | 0.46 |
                       - | XGBoost (tuned) | 0.80 | 0.47 | 0.51 |
                      
                       - XGBoost selected as final model. Hyperparameters tuned via Bayesian search (Optuna).
                      
                       - ### SHAP explainability
                       - - Global: SHAP summary plot showing top 20 features ranked by mean absolute impact
                         - - Local: Waterfall plot for individual predictions — explains each applicant decision
                           - - Interaction effects: SHAP dependence plots for top 3 feature pairs
                            
                             - Key drivers: external credit score, bureau derogatory marks, and annuity-to-income ratio explain ~58% of model variance.
                            
                             - ### Probability calibration
                             - - Platt scaling and isotonic regression compared on validation set
                               - - Reliability diagrams confirm calibrated probabilities are trustworthy for pricing use
                                 - - Final model: XGBoost + isotonic calibration
                                  
                                   - ---

                                   ## Key result

                                   The final model identifies **51% of eventual defaults in the top-risk decile** — a 5x lift over random selection. At a 0.3 threshold, precision is 0.48 and recall is 0.61, suitable for proactive outreach campaigns.

                                   ---

                                   ## File structure

                                   ```
                                   Credit Risk Modeling Projects/
                                   └── Credit Default Prediction Using Logistic Regression and XGBoost/
                                       ├── README.md
                                       ├── Notebooks/
                                       │   ├── 01_eda.ipynb
                                       │   ├── 02_feature_engineering.ipynb
                                       │   ├── 03_modeling_comparison.ipynb
                                       │   └── 04_shap_explainability.ipynb
                                       ├── Scripts/
                                       │   ├── features.py
                                       │   └── evaluate.py
                                       └── data/
                                           └── application_train_sample.csv
                                   ```

                                   ---

                                   ## Skills demonstrated

                                   `Python` · `XGBoost` · `scikit-learn` · `SHAP` · `Optuna` · `imbalanced-learn` · `SMOTE` · `logistic regression` · `model calibration` · `Pandas` · `Matplotlib` · `credit risk modeling`

                                   ---

                                   *Data sourced from the publicly available Home Credit Kaggle competition. No proprietary data used.*

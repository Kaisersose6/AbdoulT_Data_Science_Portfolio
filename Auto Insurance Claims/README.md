# Auto Insurance Claims — Frequency & Severity Modeling

**Domain:** Actuarial science · Insurance analytics · **Stack:** Python · GLMs · Survival analysis · scikit-learn

---

## Overview

I built this project to demonstrate actuarial-grade insurance claims modeling — the same statistical foundation underlying premium pricing at every major P&C insurer. The pipeline models both claims frequency (how often a policyholder files a claim) and claims severity (how much each claim costs) separately, then combines them into an expected loss estimate per policy.

This project draws on my actuarial science background from my B.S. at UTSA and reflects the kind of statistical rigor I applied at Pearson and Wells Fargo in regulated, high-stakes analytical environments.

---

## Business problem

Auto insurers face two core pricing challenges:

1. **Adverse selection** — charging the same premium to high-risk and low-risk policyholders leads to losses as high-risk customers self-select in
2. **Underpricing severity** — even correctly predicted claim frequency is useless if the cost-per-claim is systematically underestimated

A two-part GLM (frequency + severity) addresses both. This project builds, evaluates, and interprets that pipeline end-to-end.

---

## Data

- Source: French Motor Third-Party Liability dataset (publicly available via OpenML / sklearn)
- ~678,000 policy-years with claims frequency and severity outcomes
- Features: vehicle age, driver age, vehicle power, region, bonus-malus score, density
- Two targets: claim count per exposure (frequency) and average claim cost (severity)

---

## Technical approach

### Claims frequency model
- Distribution: Poisson regression with log link and exposure offset
- Accounts for varying policy durations (exposure) — a critical actuarial adjustment often missing from non-actuarial ML work
- Evaluated via deviance, Pearson chi-squared, and lift curves by risk decile

### Claims severity model
- Distribution: Gamma regression with log link (right-skewed, strictly positive cost distribution)
- Trained only on policies with at least one claim
- Evaluated via mean absolute error and relative error by cost percentile

### Combined pure premium
- Pure premium = E[frequency] x E[severity] per policy
- Gini coefficient and double-lift chart assess combined model discrimination

### Survival analysis (time-to-first-claim)
- Kaplan-Meier curves by risk segment
- Cox proportional hazards model to identify significant time-varying risk factors
- Log-rank test to confirm statistical significance of segment differences

### Gradient boosting comparison
- XGBoost trained on same features for frequency prediction
- Compared against Poisson GLM on held-out test set
- GLM preferred for interpretability and regulatory defensibility despite marginal XGBoost lift

---

## Results

| Model | Metric | Score |
|---|---|---|
| Poisson GLM (frequency) | Deviance ratio | 0.18 |
| Gamma GLM (severity) | Mean absolute error | $412 |
| Combined pure premium | Gini coefficient | 0.34 |
| XGBoost frequency | ROC-AUC vs GLM | +0.02 lift |

Top risk drivers: bonus-malus score, driver age under 25, vehicle power above 120hp.

---

## File structure

```
Auto Insurance Claims/
├── README.md
├── Notebooks/
│   ├── 01_eda_and_exposure.ipynb
│   ├── 02_frequency_poisson_glm.ipynb
│   ├── 03_severity_gamma_glm.ipynb
│   ├── 04_pure_premium_combined.ipynb
│   └── 05_survival_analysis.ipynb
└── data/
    └── freMTPL2freq.csv
    ```

    ---

    ## Skills demonstrated

    `Python` · `statsmodels` · `GLMs` · `Poisson regression` · `Gamma regression` · `exposure modeling` · `survival analysis` · `Kaplan-Meier` · `Cox proportional hazards` · `XGBoost` · `actuarial pricing` · `Pandas` · `Matplotlib`

    ---

    *Uses the publicly available French MTPL dataset. Methodology follows actuarial pricing standards for P&C insurance.*

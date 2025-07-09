# 🛡️ RiskGuardian AI — Real-Time Risk Detection from SEC Filings

**RiskGuardian AI** is an advanced NLP-powered compliance and risk intelligence pipeline designed to automatically detect and classify emerging risks (e.g. cybersecurity, financial instability, regulatory issues) from SEC 10-K and 10-Q filings using zero-shot learning and large language models.

---

## 🚀 Project Overview

| Component            | Purpose                                                                 |
|---------------------|-------------------------------------------------------------------------|
| `00_setup.ipynb`        | Fetch and save SEC filings (10-K/10-Q) for selected companies           |
| `01_preprocess.ipynb`   | Clean and standardize filing text for NLP processing                    |
| `02_nlp_risk_classification.ipynb` | Classify risk types using Hugging Face zero-shot model (BART-MNLI)  |
| `03_visualize_dashboard.py`     | Streamlit dashboard to explore risk breakdown by company         |

---

## 🎯 Problem This Solves

Public company filings are massive, legal-heavy documents that bury crucial risk disclosures. RiskGuardian AI automates:
- Monitoring of emerging risks across financial filings
- Early detection of risk signals for analysts, investors, and regulators
- Scalable compliance screening for enterprise portfolios

---

## 🔍 Features

- ✅ **Real SEC Data**: Pulls live 10-K/10-Q filings from the SEC EDGAR index
- 🤖 **Zero-shot NLP**: Classifies risk mentions without retraining using `facebook/bart-large-mnli`
- 📊 **Visual Dashboard**: Interactive Streamlit dashboard to explore risks by company
- 📦 **Modular Architecture**: Ready for Airflow scheduling and cloud deployment
- 🔐 **Compliance Logging**: Tracks skipped companies and failed filings

---

## 📂 Folder Structure

RiskGuardian_AI/
│
├── data/
│ ├── raw/ # Downloaded SEC filings
│ ├── processed/ # Cleaned text and model outputs
│ └── logs/ # Skipped or failed CIKs
│
├── models/ # Future expansion (LLMs, fine-tuned risk detectors)
├── artifacts/ # Intermediate outputs
│
├── 00_setup.py # Index + 10-K/10-Q crawler
├── 01_preprocess.py # Data cleaner
├── 02_nlp_risk_classification.py
├── 03_visualize_dashboard.py
└── airflow/ (IP)
└── dags/ (IP)
└── riskguardian_dag.py (optional)

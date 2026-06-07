# RiskGuardian AI — NLP Risk Detection from SEC Filings

**Domain:** Financial risk · Regulatory NLP · **Stack:** Python · BART-MNLI · Streamlit

---

## Overview

I built RiskGuardian AI to show how zero-shot NLP can extract and classify risk signals from SEC 10-K and 10-Q filings at scale — without requiring labeled training data. Public company filings disclose material risks in dense legal language that analysts struggle to monitor consistently. This pipeline automates that work, classifying each risk passage by type and surfacing emerging threats across a portfolio of companies.

The project connects directly to skills I applied at Wells Fargo, where I used NLP and statistical analysis to identify fraud patterns and improve analytical accuracy across regulatory data pipelines.

---

## Business problem

Institutional analysts, compliance teams, and investors need to monitor dozens or hundreds of companies for emerging risks — cybersecurity breaches, financial instability, litigation exposure, and regulatory changes. Reading every 10-K manually doesn't scale. This project answers:

1. What risk types are disclosed in a given filing, and how prominently?
2. 2. How has a company's risk profile shifted between quarters?
   3. 3. Which companies in a portfolio show the highest concentration of a specific risk type?
     
      4. ---
     
      5. ## Technical approach
     
      6. ### Data collection (`00_setup.ipynb`)
      7. Fetches SEC 10-K and 10-Q filings via the SEC EDGAR API for a configurable list of companies and date ranges. Saves raw filing text locally for reproducibility.
     
      8. ### Preprocessing (`01_preprocess.ipynb`)
      9. - Extracts the "Risk Factors" section from each filing using regex and heuristic section detection
         - - Splits risk disclosures into sentence-level chunks for granular classification
           - - Cleans and standardizes text: removes boilerplate, normalizes whitespace, strips HTML artifacts
            
             - ### Zero-shot risk classification (`02_nlp_risk_classification.ipynb`)
             - Uses Hugging Face's `facebook/bart-large-mnli` zero-shot classification model to assign each risk passage to one or more of seven risk categories:
            
             - | Risk category | Example disclosure signal |
             - |---|---|
             - | Cybersecurity | "unauthorized access to our systems" |
             - | Financial instability | "liquidity constraints", "covenant violations" |
             - | Regulatory / legal | "pending investigations", "new compliance requirements" |
             - | Operational | "supply chain disruptions", "key personnel loss" |
             - | Market / competitive | "pricing pressure", "loss of market share" |
             - | Macroeconomic | "inflation", "interest rate exposure" |
             - | ESG / climate | "climate-related regulations", "carbon emissions" |
            
             - No fine-tuning required — BART-MNLI's natural language inference capability generalizes directly to this task.
            
             - ### Visualization dashboard (`03_visualize_dashboard.py`)
             - Interactive Streamlit app showing:
             - - Risk category breakdown by company (stacked bar chart)
               - - Time-series view of risk concentration across quarters
                 - - Side-by-side comparison of two companies' risk profiles
                   - - Raw passage viewer with classification scores
                    
                     - ---

                     ## Results

                     Tested on filings from 10 S&P 500 companies across 8 quarters:

                     - **Classification accuracy:** 84% agreement with manually labeled sample of 200 passages
                     - - **Processing speed:** ~45 seconds per 10-K filing end-to-end
                       - - **Key finding:** Cybersecurity and macroeconomic risk disclosures increased significantly in 2022-2023 filings vs. 2020-2021 baseline across the test portfolio
                        
                         - ---

                         ## File structure

                         ```
                         riskguardian_AI/
                         ├── README.md
                         ├── Notebooks/
                         │   ├── 00_setup.ipynb
                         │   ├── 01_preprocess.ipynb
                         │   └── 02_nlp_risk_classification.ipynb
                         ├── data/
                         │   ├── raw_filings/
                         │   └── processed/
                         ├── 03_visualize_dashboard.py
                         └── requirements.txt
                         ```

                         ---

                         ## Running the project

                         ```bash
                         pip install -r requirements.txt

                         # Fetch filings (configure companies in 00_setup.ipynb)
                         jupyter notebook Notebooks/00_setup.ipynb

                         # Run full pipeline
                         jupyter notebook Notebooks/01_preprocess.ipynb
                         jupyter notebook Notebooks/02_nlp_risk_classification.ipynb

                         # Launch dashboard
                         streamlit run 03_visualize_dashboard.py
                         ```

                         ---

                         ## Skills demonstrated

                         `Python` · `Hugging Face Transformers` · `BART-MNLI` · `zero-shot classification` · `NLP` · `SEC EDGAR API` · `regex text extraction` · `Streamlit` · `Pandas` · `regulatory data analysis`

                         ---

                         *Uses publicly available SEC EDGAR filings. No proprietary data. Reproducible end-to-end.*

# MARS: Marketing Attribution & Revenue Simulation

**Domain:** Marketing science · Media mix modeling · Budget optimization

---

## Overview

I built MARS to demonstrate a full Bayesian Marketing Mix Modeling pipeline — from raw media spend data through channel attribution, adstock decay, ROI decomposition, and scenario-based budget optimization. The project mirrors modeling I led at Harland Clarke and AMSIVE, where attribution models directly informed client media spend decisions worth millions in annual budget.

Unlike black-box attribution tools, MARS is fully transparent: every channel's contribution is quantified with a posterior distribution, not a point estimate, so you can see exactly how certain the model is about each channel's effect.

---

## Business problem

Marketing teams routinely allocate budget across TV, digital, paid search, email, and social without a rigorous view of which channels drive revenue. This project answers three questions:

1. What share of revenue is attributable to each channel vs. baseline organic demand?
2. 2. How does advertising effect decay over time — and how quickly?
   3. 3. Given a fixed total budget, what allocation maximizes projected revenue?
     
      4. ---
     
      5. ## Technical approach
     
      6. ### Adstock transformation (`adstock.py`)
      7. Models the carryover effect of ad spend using a geometric decay function. Each channel has its own fitted decay rate, capturing how long an impression continues influencing consumer behavior after exposure.
     
      8. ### Bayesian MMM (`02_bayesian_mmm.py`)
      9. Fits a Bayesian linear model using PyMC with hierarchical priors on channel coefficients, adstock-transformed spend as predictors, posterior sampling via NUTS, and credible intervals on all attribution estimates. This gives honest uncertainty quantification that frequentist MMM cannot — critical when presenting to skeptical stakeholders.
     
      10. ### Budget optimizer (`04_budget_optimizer.py`)
      11. Uses the fitted model's posterior means to solve a constrained optimization: maximize expected revenue subject to a fixed total spend. Implements both gradient-based (scipy.optimize) and grid-search approaches.
     
      12. ### Scenario dashboard (`05_dashboard.py`)
      13. Interactive Streamlit dashboard: adjust channel spend sliders and see projected revenue in real time, compare current vs. optimized allocation, and view a channel contribution waterfall chart.
     
      14. ### Report generator (`06_report_generator.py`)
      15. Automated PDF report summarizing model fit, channel attributions with credible intervals, and optimization recommendations — ready for client delivery.
     
      16. ---
     
      17. ## Results summary
     
      18. | Channel | Attribution share | 90% credible interval | Recommended change |
      19. |---|---|---|---|
      20. | Paid search | 34% | [29%, 39%] | +8% budget |
      21. | TV / video | 22% | [16%, 28%] | No change |
      22. | Email | 18% | [15%, 21%] | +5% budget |
      23. | Paid social | 14% | [9%, 19%] | -10% budget |
      24. | Display | 12% | [7%, 17%] | -3% budget |
     
      25. Optimized allocation projects a **+12% revenue lift** at the same total spend.
     
      26. ---
     
      27. ## File structure
     
      28. ```
          MARS_MMM/
          ├── README.md
          ├── 01_synthetic_data_generator.py
          ├── 02_bayesian_mmm.py
          ├── 04_budget_optimizer.py
          ├── 05_dashboard.py
          ├── 06_report_generator.py
          ├── adstock.py
          ├── config.py
          └── requirements.txt
          ```

          ---

          ## Running the project

          ```bash
          pip install -r requirements.txt
          python 01_synthetic_data_generator.py
          python 02_bayesian_mmm.py
          streamlit run 05_dashboard.py
          ```

          ---

          ## Skills demonstrated

          `Python` · `PyMC` · `Bayesian inference` · `MCMC` · `adstock modeling` · `constrained optimization` · `scipy.optimize` · `Streamlit` · `marketing mix modeling` · `uncertainty quantification` · `automated PDF reporting`

          ---

          *Synthetic data generated for portfolio purposes. Methodology mirrors production MMM work done at AMSIVE and Harland Clarke supporting $10M+ annual media budgets.*

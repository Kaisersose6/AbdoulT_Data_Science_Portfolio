import streamlit as st
import pandas as pd
import os

companies = {
    "Apple": "0000320193",
    "Microsoft": "0000789019",
    "Meta": "0001326801",
    "Amazon": "0001018724",
    "Google": "0001652044",
    "Rise": "0001640967",
    "Tesla": "0001318605",
    "Nvidia": "0001045810"
}

import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*ScriptRunContext.*")


st.set_page_config(page_title="RiskGuardian Dashboard", layout="wide")
st.title("📊 Risk Classification Explorer — SEC Filings")

selected_company = st.selectbox("Choose a company to view risk breakdown:", list(companies.keys()))

risk_file = f"../data/processed/{selected_company}_filing_risk_labels.csv"

if os.path.exists(risk_file):
    df = pd.read_csv(risk_file)
    st.subheader(f"Risk Profile for {selected_company}")
    st.dataframe(df.style.background_gradient(cmap="Reds", subset=["score"]))
    st.bar_chart(df.set_index("risk_label")['score'])
else:
    st.warning(f"No risk data available for {selected_company}. Please check the log or rerun earlier steps.")
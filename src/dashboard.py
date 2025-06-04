import streamlit as st
import pandas as pd
from model import load_model
from data_loader import load_data
from optimizer import optimize_cost

st.set_page_config(page_title="Cost Optimizer", layout="wide")
st.title("💰 AI-Based Infrastructure Cost Optimizer")

data = load_data("data/sample_usage.csv")
model = load_model()
recommendations = optimize_cost(data, model)

st.subheader("📊 Full Usage and Cost Data")
st.dataframe(data)

st.subheader("✅ Optimization Recommendations")
if not recommendations.empty:
    st.dataframe(recommendations)
    st.bar_chart(recommendations.set_index('resource_id')['potential_savings'])
else:
    st.success("No cost optimizations needed! ✅")


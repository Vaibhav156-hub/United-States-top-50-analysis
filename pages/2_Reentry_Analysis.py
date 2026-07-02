import streamlit as st
import pandas as pd

st.title("🔄 Chart Re-Entry Analysis")

df = pd.read_csv("data/processed_dataset.csv")

st.subheader("Top Songs by Re-Entry Count")

top = (
    df.groupby(["song","artist"])["Reentry_Count"]
    .max()
    .reset_index()
    .sort_values("Reentry_Count", ascending=False)
)

st.dataframe(top.head(20), use_container_width=True)

st.subheader("Distribution of Re-Entries")

st.bar_chart(top["Reentry_Count"].value_counts().sort_index())
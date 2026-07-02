import streamlit as st
import pandas as pd

df = pd.read_csv("data/processed_dataset.csv")

st.title("🏠 Dashboard Overview")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Records", len(df))
col2.metric("Songs", df["song"].nunique())
col3.metric("Artists", df["artist"].nunique())
col4.metric("Average Popularity", round(df["popularity"].mean(),2))

st.divider()

st.subheader("Dataset Preview")

st.dataframe(df.head(20), use_container_width=True)

st.subheader("Dataset Statistics")

st.write(df.describe())
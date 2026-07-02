import streamlit as st
import pandas as pd

st.title("📈 Momentum Analysis")

df = pd.read_csv("data/processed_dataset.csv")

st.subheader("Top Momentum Songs")

top = df.sort_values(
    "Momentum_Score",
    ascending=False
)[
["song","artist","Momentum_Score","position"]
].head(20)

st.dataframe(top, use_container_width=True)

st.subheader("Momentum Score Distribution")

st.line_chart(df["Momentum_Score"])
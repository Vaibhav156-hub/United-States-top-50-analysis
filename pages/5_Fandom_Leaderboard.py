import streamlit as st
import pandas as pd

st.title("❤️ Fandom Leaderboard")

df = pd.read_csv("data/processed_dataset.csv")

leader = (
    df.groupby("artist")
    .agg(
        Fandom=("Fandom_Intensity_Score","mean"),
        Reentries=("Reentry_Count","max")
    )
    .sort_values("Fandom", ascending=False)
)

st.dataframe(leader.head(20), use_container_width=True)
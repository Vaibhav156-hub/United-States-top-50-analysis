import streamlit as st
import pandas as pd

st.title("💿 Content Analysis")

df = pd.read_csv("data/processed_dataset.csv")

album = (
    df.groupby("album_type")
    .agg(
        Avg_Momentum=("Momentum_Score","mean"),
        Avg_Fandom=("Fandom_Intensity_Score","mean")
    )
)

st.dataframe(album)

st.bar_chart(album)
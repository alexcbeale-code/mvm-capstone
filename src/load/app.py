import streamlit as st
import pandas as pd

st.title("This Is A Title!")

df = pd.read_feather("data/processed/ready_data.feather")

st.dataframe(df)

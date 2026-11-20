import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('sessions.csv')

st.title("🧬 CodeDNA")
st.write("Discover your coding fingerprint!")

total_minutes = df['minutes'].sum()

st.metric('Total Coding Time', total_minutes)
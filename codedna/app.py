import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('sessions.csv')

fig = px.bar(
    df,
    x='minutes',
    y='day',
    title='My coding Activity'
)

st.title("🧬 CodeDNA")
st.write("Discover your coding fingerprint!")

total_minutes = df['minutes'].sum()
average_length = df['minutes'].mean()

st.metric('Total Coding Time', total_minutes)
st.metric('Average Time', average_length)

st.plotly_chart(fig)
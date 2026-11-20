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
language_totals = df.groupby('language')['minutes'].sum().reset_index()

st.metric('Total Coding Time', total_minutes)
st.metric('Average Time', average_length)

fig = px.bar(
    df,
    x='minutes',
    y='day',
    title='My coding Activity'
)
fig_two = px.bar(
    language_totals,
    x='language',
    y = 'minutes',
    title='Total of Languages'
)

st.plotly_chart(fig)
st.plotly_chart(fig_two)
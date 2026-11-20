'''
this is the structure for pandas:
import pandas as pd
df = pd.DataFrame(sessions)
print(df)
---------------------------------------------
.sum() adds the numbers.
.mean() calculates the average.
.max() finds the largest value.
---------------------------------------------
To learn about the total time spent coding here:
total_minutes = df["minutes"].sum()
print(total_minutes)
'''

import pandas as pd
import plotly.express as px

df = pd.read_csv("sessions.csv")

print(df)

total_minutes = df["minutes"].sum()
average_length = df["minutes"].mean()
longest_session = df["minutes"].max()

# Keep your remaining calculations here!

pyhton_sessions = df[df['language'] == 'Python']
python_minutes = pyhton_sessions['minutes'].sum()
javascript_session = df[df["language"] == 'JavaScript']
javascript_minutes = javascript_session['minutes'].sum()

if javascript_minutes > python_minutes:
    print('Most practiced language is JavaScript')
else:
    print('Most practiced language is Python')

print(f'Total python minutes are :{python_minutes} minutes' )
print(f'Total JavaScript minutes are :{javascript_minutes} minutes' )
print(f'Total minutes is : {total_minutes} minutes ')
print(f'Average length is : {average_length} minutes')
print(f'Longest session is : {longest_session} minutes')

print(df)


fig = px.bar(
    df,
    x="minutes",
    y="day",
    title="My Coding Activity"
)

fig.show()

language_totals = df.groupby("language")["minutes"].sum().reset_index()

print(language_totals)

fig_two = px.bar(
    language_totals ,
    x= 'language',
    y= 'minutes',
    title= 'New group Activity'
)

fig_two.show()
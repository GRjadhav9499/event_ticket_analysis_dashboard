import numpy as np 
import pandas as pd
import os
import plotly.express as px
import streamlit as st


# data preprocessing
df = pd.read_csv('./incident_event_log.csv').head(5000)
df = df[df['incident_state'] == 'Closed']
df.replace('?', pd.NA, inplace=True)  
df['opened_at'] = pd.to_datetime(df['opened_at'], errors='coerce')
df['sys_created_at'] = pd.to_datetime(df['sys_created_at'], errors='coerce')
df['sys_updated_at'] = pd.to_datetime(df['sys_updated_at'], errors='coerce')
df['resolved_at'] = pd.to_datetime(df['resolved_at'], errors='coerce')
df['closed_at'] = pd.to_datetime(df['closed_at'], errors='coerce')
df['time_to_resolve'] = df['resolved_at'] - df['opened_at']


incident_state = st.sidebar.multiselect(
    "incident_state : ",
    options=df['incident_state'].unique(),
    default=df['incident_state'].unique()
)

reassignment_count = st.sidebar.multiselect(
    "reassignment_count : ",
    options=df['reassignment_count'].unique(),
    default=df['reassignment_count'].unique()
)

reopen_count = st.sidebar.multiselect(
    "reopen_count: ",
    options=df['reopen_count'].unique(),
    default=df['reopen_count'].unique()
)

made_sla = st.sidebar.multiselect(
    "made_sla: ",
    options=df['made_sla'].unique(),
    default=df['made_sla'].unique()
)
impact = st.sidebar.multiselect(
    "impact : ",
    options=df['impact'].unique(),
    default=df['impact'].unique()
)
urgency = st.sidebar.multiselect(
    "urgency: ",
    options=df['urgency'].unique(),
    default=df['urgency'].unique()
)
priority = st.sidebar.multiselect(
    "priority: ",
    options=df['priority'].unique(),
    default=df['priority'].unique()
)



df_selection = df.query(
    " reassignment_count == @reassignment_count &  reopen_count == @reopen_count & made_sla == @made_sla & impact == @impact & urgency == @urgency & priority == @priority"
)

# -----MAIN PAGE-------

# Set the main page title and headers
st.title(":bar_chart: SYSTEM TICKETS DASHBOARD ")
st.markdown("##")

# Calculate and display top KPIs
total_records_in_system = df['number'].max()
# average_age = round(df_selection['Customer Age'].mean(), 1)
records_selected_currently = df_selection.shape[0]

# Create 3 columns to display KPIs side by side
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("TOTAL RECORDS : ")
    st.subheader(f"{total_records_in_system}")
with middle_column:
    st.subheader("AVERAGE CUSTOMER AGE : ")
    st.subheader("0000")
with right_column:
    st.subheader("RECORDS SELECTED CURRENTLY : ")
    st.subheader(f"{records_selected_currently}")


st.markdown("---")

fig = px.bar(df_selection, y='reassignment_count', title='Ticket Priority Count Plot', orientation='h')
fig.update_traces(marker=dict(color='orange'), opacity=0.8, hovertemplate="%{y}: %{x}")
fig.update_layout(title_font=dict(size=24), yaxis_title="reassignment_count", xaxis_title="Count", title_x=0.5)
st.plotly_chart(fig)

# fig = px.histogram(df_selection, x='reassignment_count', title='reassignment_countHistogram')
# fig.update_traces(marker=dict(color='royalblue'), opacity=0.8, hovertemplate="%{x}: %{y}")
# fig.update_layout(title_font=dict(size=24), xaxis_title="reassignment_count", yaxis_title="Count", title_x=0.5)
# st.plotly_chart(fig)


pie_chart_data = df_selection['made_sla'].value_counts()
fig = px.pie(pie_chart_data, names=pie_chart_data.index, values=pie_chart_data.values)
fig.update_traces(marker=dict(colors=['royalblue', 'pink']), hoverinfo='label+percent', textinfo='percent', textfont_size=14)
fig.update_layout(title_text='made_sla')
st.plotly_chart(fig)# Create the Scatter Plot for Ticket Type and Customer Age


fig = px.scatter(df_selection, x='reassignment_count', y='made_sla', color='priority',
                 title='Scatter Plot for ----')
fig.update_traces(marker=dict(size=12, opacity=0.8), selector=dict(mode='markers'),
                  hovertemplate="%{x}: %{y} years, Priority: %{marker.color}")
fig.update_layout(title_font=dict(size=24), xaxis_title="Ticket Type", yaxis_title="Customer Age",
                  title_x=0.5, legend_title="Ticket Priority", legend_traceorder='reversed')
st.plotly_chart(fig)
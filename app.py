import numpy as np 
import pandas as pd
import os
import plotly.express as px
import streamlit as st



############################# utils ###################################
st.set_page_config(
    page_title="Event tickets data analysis",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",  
)

def preprocess_data(df):
    df = df[df['incident_state'] == 'Closed']
    df.replace('?', pd.NA, inplace=True)  
    df['opened_at'] = pd.to_datetime(df['opened_at'], errors='coerce')
    df['sys_created_at'] = pd.to_datetime(df['sys_created_at'], errors='coerce')
    df['sys_updated_at'] = pd.to_datetime(df['sys_updated_at'], errors='coerce')
    df['resolved_at'] = pd.to_datetime(df['resolved_at'], errors='coerce')
    df['closed_at'] = pd.to_datetime(df['closed_at'], errors='coerce')
    df['time_to_resolve'] = df['resolved_at'] - df['opened_at']
    df["time_to_resolve_hours"] = df["time_to_resolve"].astype('timedelta64[s]') / 3600
    df["time_to_resolve_hours"] = df["time_to_resolve"].astype('timedelta64[s]') / 3600
    df.loc[df["time_to_resolve_hours"] < 0, "time_to_resolve_hours"] = 0
    return df

def show_value_counts(df, column):
    fig1 = px.bar(
        df[column].value_counts().reset_index(),
        x=column,
        y='index',
        orientation='h',
        title=f'{column} Counts',
        labels={'index': column, column: 'Count'}
    )
    return st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

def show_tabs_with_value_counts(df, column_names):
    tabs = st.tabs(column_names)
    for i, tab_column in enumerate(column_names):
        with tabs[i]:
            show_value_counts(df, tab_column)

############################# data preprocessing ###########################

df = pd.read_csv('./incident_event_log.csv')
df = preprocess_data(df)

# sidebar
knowledge = st.sidebar.multiselect(
    "knowledge : ",
    options=df['knowledge'].unique(),
    default=df['knowledge'].unique()
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

# select df based on sidebar
df_selection = df.query(
    " knowledge == @knowledge & reassignment_count == @reassignment_count &  reopen_count == @reopen_count & made_sla == @made_sla & impact == @impact & urgency == @urgency & priority == @priority"
)

# ----------------------------- MAIN PAGE -------------------------------------

# title and header
st.title(":bar_chart: SYSTEM TICKETS DASHBOARD ")
st.markdown("##")

# Top KPI
total_records_in_system = df.shape[0]
records_selected_currently = df_selection.shape[0]

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("TOTAL RECORDS: ")
    st.success(f"{total_records_in_system}")
with right_column:
    st.subheader("RECORDS SELECTED CURRENTLY: ")
    st.success(f"{records_selected_currently}")

########################## charts ##############################

st.markdown("---")

st.subheader("Tabs")

column_names = ["category", 'subcategory', "reassignment_count", "reopen_count",
                "impact", "urgency", "priority",'contact_type','location']

show_tabs_with_value_counts(df_selection, column_names)


# pie
pie_chart_data = df_selection['made_sla'].value_counts()
fig = px.pie(pie_chart_data, names=pie_chart_data.index, values=pie_chart_data.values)
fig.update_traces(marker=dict(colors=['royalblue', 'pink']), hoverinfo='label+percent', textinfo='percent', textfont_size=14)
fig.update_layout(title_text='SLA breached?')
st.plotly_chart(fig)# Create the Scatter Plot for Ticket Type and Customer Age

# pie
pie_chart_data = df_selection['knowledge'].value_counts()
fig = px.pie(pie_chart_data, names=pie_chart_data.index, values=pie_chart_data.values)
fig.update_traces(marker=dict(colors=['royalblue', 'pink']), hoverinfo='label+percent', textinfo='percent', textfont_size=14)
fig.update_layout(title_text='Knowledge available?')
st.plotly_chart(fig)# Create the Scatter Plot for Ticket Type and Customer Age


# scatter plot 
X_AXIS = 'reopen_count'
Y_AXIS = 'reassignment_count'
COLOR = 'priority'

fig = px.scatter(df_selection, x=X_AXIS, y=Y_AXIS, color=COLOR,
                 title='What kind of INC getting reassigned/reopened?')

fig.update_traces(marker=dict(size=12, opacity=0.8), selector=dict(mode='markers'),
                  hovertemplate="%{x}: %{y} , Priority:")

fig.update_layout(title_font=dict(size=24), xaxis_title=X_AXIS, yaxis_title=Y_AXIS,
                  title_x=0.5, legend_title="Ticket Priority", legend_traceorder='reversed')

fig.update_layout(title=dict(x=0.1, y=0.9)) 

st.plotly_chart(fig)

import numpy as n
import pandas as pd
import plotly.express as px
import streamlit as st

############################# utils ###################################

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
######################### data preprocessing ##########################

df = pd.read_csv('./incident_event_log.csv')

# Select only closed
df = df[df['incident_state'] == 'Closed']

# replace ? with NAN
df.replace('?', pd.NA, inplace=True)  

#convert to datetime
df['opened_at'] = pd.to_datetime(df['opened_at'], errors='coerce')
df['sys_created_at'] = pd.to_datetime(df['sys_created_at'], errors='coerce')
df['sys_updated_at'] = pd.to_datetime(df['sys_updated_at'], errors='coerce')
df['resolved_at'] = pd.to_datetime(df['resolved_at'], errors='coerce')
df['closed_at'] = pd.to_datetime(df['closed_at'], errors='coerce')

# calculate time_to_resolve
df['time_to_resolve'] = df['resolved_at'] - df['opened_at']

########################## Value counts ##############################
st.subheader("Value Counts")

column_names = ["category", 'subcategory',"incident_state", "reassignment_count", "reopen_count",
                "impact", "urgency", "priority", "made_sla", "knowledge"]

show_tabs_with_value_counts(df, column_names)


########################## which kind of INC gettting reopened ? ##############################

reopened_df = df[df["reopen_count"] > 0]

st.subheader("Which kind of INC gettting Reopened ?")

column_names = ["category", 'subcategory','priority',
                'assignment_group','assigned_to','knowledge','closed_code',
                'resolved_by']

show_tabs_with_value_counts(reopened_df, column_names)


########################## which kind of INC gettting Reassigned ? ##############################

reassigned_df = df[df["reassignment_count"] > 0]

st.subheader("Which kind of INC gettting Reassigned ?")

column_names = ["category", 'subcategory','priority',
                'assignment_group','assigned_to','knowledge','closed_code',
                'resolved_by']

show_tabs_with_value_counts(reassigned_df, column_names)


########################## which kind of INC missing SLA? ##############################

sla_df = df[df["made_sla"] == 1 ]

st.subheader("Which kind of INC missing the SLA's?")

column_names = ["category", 'subcategory','priority',
                'assignment_group','assigned_to','knowledge','closed_code',
                'resolved_by']

show_tabs_with_value_counts(sla_df, column_names)
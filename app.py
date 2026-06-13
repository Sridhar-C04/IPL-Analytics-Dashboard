import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(
    page_title="IPL 2026 Analytics Dashboard",
    page_icon="🏏",
    layout="wide"
)

# Load Data
df = pd.read_csv("IPL_2026_Data.csv",encoding="latin-1")

# Title
st.title("🏏 IPL 2026 Analytics Dashboard")
st.markdown("### IPL Match Analysis & Insights")

# Sidebar
st.sidebar.header("Filters")

selected_team = st.sidebar.selectbox(
    "Select Team",
    ["All"] + sorted(list(set(df["Team1"]).union(set(df["Team2"]))))
)

# Filter Data
filtered_df = df.copy()

if selected_team != "All":
    filtered_df = filtered_df[
        (filtered_df["Team1"] == selected_team) |
        (filtered_df["Team2"] == selected_team)
    ]

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Matches", filtered_df["Match_No"].nunique())

with col2:
    st.metric("Venues", filtered_df["Venue"].nunique())

with col3:
    st.metric("Cities", filtered_df["Venue_city"].nunique())

with col4:
    st.metric("Winners", filtered_df["Match_winner"].nunique())

st.divider()

# Charts
col1, col2 = st.columns(2)

with col1:

    wins = filtered_df["Match_winner"].value_counts()

    fig = px.bar(
        x=wins.index,
        y=wins.values,
        text=wins.values,
        title="Team Wise Wins"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    toss = filtered_df["Toss_winner_decision"].value_counts()

    fig = px.pie(
        values=toss.values,
        names=toss.index,
        hole=0.5,
        title="Toss Decision Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# Venue Analysis

venue = filtered_df["Venue_city"].value_counts().head(10)

fig = px.bar(
    x=venue.index,
    y=venue.values,
    text=venue.values,
    title="Top Match Cities"
)

st.plotly_chart(fig, use_container_width=True)

# Player of Match

pom = filtered_df["Player_of_the_match"].value_counts().head(10)

fig = px.bar(
    x=pom.index,
    y=pom.values,
    text=pom.values,
    title="Top Player of the Match Winners"
)

st.plotly_chart(fig, use_container_width=True)
import streamlit as st
import pandas as pd
import preprocesseor, helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/home/abdollatif/Desktop/ODA/athlete_events.csv')
region_df = pd.read_csv('/home/abdollatif/Desktop/ODA/noc_regions.csv')

df = preprocesseor.preprocess(df, region_df)
st.sidebar.title("Olympic Analysis")
user_menu = st.sidebar.radio(
    'select an option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Atlete wise Analysis')
)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years, country = helper.country_year_list(df)

    select_year = st.sidebar.selectbox("select year", years)
    select_country = st.sidebar.selectbox("select country", country)

    medal_tally = helper.fetch_medal_tally(df, select_year, select_country)
    if select_country == 'Overall' and select_year == 'Overall':
        st.title("Overall Tally")
    if select_country == 'Overall' and select_year != 'Overall':
        st.title("Medal Tally in " + str(select_year) + " Olympics")
    if select_country != 'Overall' and select_year == 'Overall':
        st.title(select_country + " Overall performance")
    if select_country != 'overall' and select_year != 'Overall':
        st.title(select_country + " Performance in " + str(select_year) + " Olympics")
    st.dataframe(medal_tally)

if user_menu == 'Overall Analysis':
    edition = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nation = df['region'].unique().shape[0]

    st.title("Top Statistic")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(edition)
    with col2:
        st.header("Cities")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col4, col5, col6 = st.columns(3)
    with col4:
        st.header("Event")
        st.title(events)
    with col5:
        st.header("Athletes")
        st.title(athletes)
    with col6:
        st.header("Nation")
        st.title(nation)

    st.title("Participating Nation Over Year")
    nation_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nation_over_time, x='Year', y='count')
    st.plotly_chart(fig)

    st.title("Event Over Year")
    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x='Year', y='count')
    st.plotly_chart(fig)

    st.title("Sports Nation Over Year")
    sports_over_time = helper.data_over_time(df, 'Sport')
    fig = px.line(sports_over_time, x='Year', y='count')
    st.plotly_chart(fig)

    st.title("Athletes Over Year")
    athletes_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athletes_over_time, x='Year', y='count')
    st.plotly_chart(fig)

    st.title("Number of Events over time(Every Sports)")
    fig, ax = plt.subplots(figsize=(20, 20))
    x = df.drop_duplicates((['Year', 'Sport', 'Event']))
    sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype(int),
                annot=True)

    st.pyplot(fig)

    st.title("Most Successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    selected_sport = st.selectbox('Select a Sport', sport_list)
    x = helper.most_successful(df, selected_sport)

    st.table(x)
if user_menu == 'Country-wise Analysis':
    st.title("Country-wise Analysis")

    country_list = df['region'].dropna().unique().tolist()
    # country_list.sort()

    selected_country = st.selectbox("select a country", country_list)

    country_df = helper.yearwise_medal_tally(df, selected_country)
    fig = px.line(country_df, x='Year', y='Medal')
    st.title(selected_country + " Medal Tally Over thr years")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in the following sports")
    pt = helper.country_event_heatmap(df,selected_country)
    fig, ax = plt.subplots(figsize = (20, 20))
    ax = sns.heatmap(pt, annot=True)
    st.pyplot(fig)

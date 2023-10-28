import streamlit as st
import pandas as pd
import preprocesseor,helper


df = pd.read_csv('/home/abdollatif/Desktop/ODA/athlete_events.csv')
region_df = pd.read_csv('/home/abdollatif/Desktop/ODA/noc_regions.csv')

df = preprocesseor.preprocess(df, region_df)
st.sidebar.title("Olympic Analysis")
user_menu = st.sidebar.radio(
                 'select an option',
                 ('Medal Tally','Overall Analysis','Country-wise Analysis','Atlete wise Analysis')
)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)
    select_year = st.sidebar.selectbox("select year",years)
    select_year = st.sidebar.selectbox("select country",country)
    medal_tally = helper.medal_tally(df)
    st.dataframe(medal_tally)
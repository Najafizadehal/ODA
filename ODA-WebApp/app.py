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
    select_country = st.sidebar.selectbox("select country",country)

    medal_tally = helper.fetch_medal_tally(df,select_year,select_country)
    if select_country == 'Overall' and select_year == 'Overall':
        st.title("Overall Tally")
    if select_country == 'Overall' and select_year != 'Overall':
        st.title("Medal Tally in " + str(select_year) + " Olympics")
    if select_country != 'Overall' and select_year == 'Overall':
        st.title(select_country + " Overall performance")
    if select_country != 'overall' and select_year != 'Overall':
        st.title(select_country + " Performance in " + str(select_year) + " Olympics")
    st.dataframe(medal_tally)
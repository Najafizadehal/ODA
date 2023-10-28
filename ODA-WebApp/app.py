import streamlit as st
import pandas as pd

st.sidebar.radio(
                 'select an option',
                 ('Medal Tally','Overall Analysis','Country-wise Analysis','Atlete wise Analysis')
)

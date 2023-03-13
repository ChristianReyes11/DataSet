import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

st.sidebar.image("Logo.png")

st.title('Recomendaciones de Anime')
st.text('BY Christian Eduardo Amaro Reyes - S19004895')


DATA_URL = ('anime.csv')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

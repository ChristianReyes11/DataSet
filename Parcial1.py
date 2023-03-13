import streamlit as st
import pandas as pd
import numpy as np
import codecs

st.sidebar.image("Logo.jpg")
st.title('BY CHRISTIAN EDUARDO AMARO REYES - S19004895')

DATE_COLUMN = 'released'
DATA_URL = ('anime.csv')


@st.cache
def load_data(nrows):
    doc = codecs.open('anime.csv', 'rU', 'latin1')
    data = pd.read_csv(doc, nrows=nrows)
    def lowercase(x): return str(x).lower()
    return data

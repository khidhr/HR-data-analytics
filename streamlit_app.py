import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


st.set_page_config(page_title="EDA app", page_icon=":pencil2:", layout="wide")


# Web App Title
st.markdown('''
# *The HR analytics*
This is the **HR dataset analytics** created in **Streamlit** using the **pandas-profiling** library.
---
''')

@st.cache_data
def load_csv():
    csv = pd.read_csv('HR-Employee-Attrition.csv')
    return csv
df = load_csv()
pr = ProfileReport(df, explorative=True,dark_mode=True)
st.header('**Input DataFrame**')
st.write(df.head())
st.write('---')
st.header('**Pandas Profiling Report**')
st_profile_report(pr)

st.markdown('''
---
built by [Halab Khidhr](https://khidhr.github.io/khidhr-portfolio/)

''')

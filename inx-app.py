import streamlit as st
import pandas as pd
import pickle

st.title('Employee Performance web app')

department = st.selectbox('Select your department', ['HR', 'R&D', 'Legal'])

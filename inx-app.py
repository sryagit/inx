import streamlit as st
import pandas as pd
import pickle

st.title('Employee Performance web app')

department = st.selectbox('Select your department', ['HR', 'R&D', 'Legal'])

no_of_trainings = st.slider('Number of Trainings', 1, 5, 1)

gender = st.radio('Gender', ['Male', 'Female'])

st.button('Predict Performance')


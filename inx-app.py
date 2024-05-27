import streamlit as st
import pandas as pd
import pickle

st.title('Employee Performance web app')
st.write("### heading 3")
st.write("## heading 2")
st.write("# heading 1")

st.title('Employee Performance Performance Performance Performance Performance Performance web app')


department = st.selectbox('Select your department', ['HR', 'R&D', 'Legal'])

no_of_trainings = st.slider('Number of Trainings', 1, 5, 1)

gender = st.radio('Gender', ['Male', 'Female'])

st.button('Predict Performance')


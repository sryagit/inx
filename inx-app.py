import streamlit as st
import pandas as pd
import pickle

st.title('Employee Performance web app')
st.write("""### h3""")
st.write("""## h3""")
st.write("""# h3""")

department = st.selectbox('Select your department', ['HR', 'R&D', 'Legal'])

no_of_trainings = st.slider('Number of Trainings', 1, 5, 1)

import streamlit as st

st.write("This is my first test")
st.write("Testing this as an update")
st.sidebar.write("This is the sidebar")
num_days=st.sidebar.slider('Number of days', 1,30,3)


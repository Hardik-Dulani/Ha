import streamlit as st
import pickle

with open('defaults.pkl', 'rb') as file:
    defaults = pickle.load(file)
st.write(defaults)
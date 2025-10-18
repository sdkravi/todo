import streamlit as st
from functions import readFile, writeFile

st.title("A to-do App")
st.subheader("This is a to-do list")
st.write("please suggest!.")

for todo in readFile():
    st.checkbox(todo)

st.text_input("", placeholder="Enter a to-do item...")

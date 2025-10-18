import streamlit as st
from functions import readFile, writeFile

todos = readFile()

def add_todo():
    todo = st.session_state["todo_input"]
    todos.append(todo)
    writeFile(todos)

st.title("A to-do App")
st.subheader("This is a to-do list")
st.write("please suggest!.")

for todo in todos:
    st.checkbox(todo)

st.text_input("", placeholder="Enter a to-do item...",key="todo_input", on_change=add_todo)


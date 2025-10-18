import streamlit as st
from functions import readFile, writeFile

todos = readFile()

def add_todo():
    todo = st.session_state["todo_input"]
    if todo.strip() == "":
        return
    todos.append(todo)
    writeFile(todos)

st.title("A to-do App")
st.subheader("This is a to-do list")
st.write("please suggest!.")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key = todo)
    if checkbox: # if checked, mark as complete
        todos.pop(index) # remove the completed todo
        writeFile(todos) # update the file
        del st.session_state[todo] # remove checkbox state
        st.rerun() # Rerun the app to reflect changes


st.text_input("", placeholder="Enter a to-do item...",key="todo_input", on_change=add_todo)


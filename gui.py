from functions import readFile, writeFile
import FreeSimpleGUI as fg
import os

if not os.path.exists('todo.txt'):
    with open('todo.txt','w') as file:
        pass


button1=fg.Button("Add") # Add Button
text=fg.Text("Enter a to-do") # Label Text
textInput=fg.InputText(key='todo') # text field for input capture

button2=fg.Button("Edit")
button3=fg.Button("Complete")
listBox=fg.Listbox(values=readFile(),enable_events=True,size=[45,10],key='todoList')



window=fg.Window("To-do App",layout=[[text],
                                     [textInput, button1],
                                     [listBox,button2,button3]])

while(True):
    event, values = window.read()
    print(event,values)
    match event:
        case fg.WINDOW_CLOSED:
            break
        case 'Add':
            if values['todo']=="":
                fg.popup("Please enter a to-do item.",title='Error!',font=("Helvetica",12))
                continue
            todos=readFile()
            todos.append(values['todo'])
            writeFile(todos)
            listBox.update(todos)
            window['todo'].update(value="")
        case 'Edit':
            try:
                todos=readFile()
                newTodo=values['todo']
                oldTodo=values['todoList'][0]
                index=todos.index(oldTodo)
                todos[index]=newTodo
                writeFile(todos)
                listBox.update(todos)
            except IndexError:
                fg.popup("Please select an item to edit.",title='Error!',font=("Helvetica",12))
        case 'Complete':
            try:
                todos=readFile()
                popTodo=values['todo']
                index=todos.index(popTodo)
                todos.pop(index)
                writeFile(todos)
                listBox.update(todos)
                textInput.update(value="")
            except ValueError:
                fg.popup("No Item is selected, please correct",title='Error!',font=("Helvetica",9))
        case 'todoList':
            try:
                selectedTodo=values['todoList'][0]
                textInput.update(value=selectedTodo)
            except IndexError:
                pass
        
window.close()

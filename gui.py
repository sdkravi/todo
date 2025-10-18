from functions import readFile, writeFile
import FreeSimpleGUI as fg



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
            todos=readFile()
            todos.append(values['todo'])
            writeFile(todos)
            listBox.update(todos)
            window['todo'].update(value="")
        case 'Edit':
            todos=readFile()
            newTodo=values['todo']
            oldTodo=values['todoList'][0]
            index=todos.index(oldTodo)
            todos[index]=newTodo
            writeFile(todos)
            listBox.update(todos)
        case 'Complete':
            todos=readFile()
            popTodo=values['todo']
            index=todos.index(popTodo)
            todos.pop(index)
            writeFile(todos)
            listBox.update(todos)
            textInput.update(value="")
            
        case 'todoList':
            selectedTodo=values['todoList'][0]
            textInput.update(value=selectedTodo)
        
window.close()

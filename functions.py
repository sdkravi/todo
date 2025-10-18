FILEPATH='todo.txt' 

def readFile(filename=FILEPATH): # read file function
    ''' this function will read a file with default argument 'file name'. '''
    with open(filename,'r') as file :
        todoList=[i.strip('\n') for i in file.readlines()]
    return todoList    



def writeFile(todoItems,filename=FILEPATH): # default parameter use at last in sequence
    with open(filename,"w") as file :
        file.writelines([i+'\n' for i in todoItems])
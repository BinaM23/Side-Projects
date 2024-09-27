#Name: Bina Mukuyamba
#Date: 09/09/24
#To do list app
#Adapted from: https://github.com/ShaunHalverson/PythonToDo/blob/main/main.py
#Original code by: ShaunHalverson
import time
tasks = []
CompletedTasks={} #to map numbers need a dictionary
#orignial index = key, task = value so that we keep the original task numbers. if used another list there would be confusion
def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
    
def listTasks():
    if not tasks:
        print("There are no tasks.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")
            
def deleteTask():
    listTasks()
    if not tasks:
        pass  #if empty just go back to original menu
    #do nothing unless list isnt empty
    else:
        try:
            taskToDelete = int(input("Enter the # to delete: "))
            if taskToDelete >= 0 and taskToDelete < len(tasks):
                tasks.pop(taskToDelete)
                print(f"Task {taskToDelete} has been removed.")
            else:
                print(f"Task #{taskToDelete} was not found.")
        except:
            print("Invalid input.")
        
def MarkComplete():
    listTasks() 
    try:
        TaskIndex=int(input("Enter the # of the task you completed: "))
        if TaskIndex>= 0 and TaskIndex < len(tasks):
            CompletedTasks[TaskIndex]=tasks[TaskIndex]
            print(f"Task {TaskIndex} has been completed.")
        else:
            print(f"Task #{TaskIndex} was not found.")
    except:
        print("Invalid input.")    
    
def ViewComplete():
    if not CompletedTasks:
        print("There are no completed tasks.")
    else:
        print("Completed tasks:")
        for index, task in CompletedTasks.items():
            print(f"Task #{index}. {task}")   
    
def reminder():
    print("These Tasks are not yet complete:")
    for index, task in enumerate(tasks):
        if task not in CompletedTasks:
            print(f"Task #{index}. {task}")    
    
if __name__=="__main__":
    #Create a loop to run app
    while True:
        print("\n")
        print("Please Select one of the following options")
        print("------------------------------------------")
        print("1. Add task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. mark task complete")
        print("5. view completed tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if (choice == "1"):
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            listTasks()
        elif (choice == "4"):
            MarkComplete()
        elif (choice == "5"): #added my own functions for completed tasks
            ViewComplete()            
        elif (choice == "6"):
            break
        else:
            print("Invalid input. Please try again.")
        #Reminder functionality every minute while tasks are not done!
        reminder()
        time.sleep(10)
        reminder()
       
    print("Goodbye 👋👋")        
        
        #can add time function to remind user of tasks left
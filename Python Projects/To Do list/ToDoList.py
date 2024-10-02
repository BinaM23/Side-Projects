#Name: Bina Mukuyamba
#Date: 09/09/24
#To do list app
#Adapted from: https://github.com/ShaunHalverson/PythonToDo/blob/main/main.py
#Original code by: ShaunHalverson
import time
#My modifications
#Mark task as complete
#View completed tasks
#Save tasks to a pdf/txt file

tasks = []
#CompletedTasks={} #to map numbers need a dictionary
#orignial index = key, task = value so that we keep the original task numbers. if used another list there would be confusion
#if we use a list of completed tasks the numbers are different
CompletedTasks=set()
def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
    
def listTasks():
    if not tasks:
        print("There are no tasks.")
    else:
        #print("Current Tasks:")
        #for index, task in enumerate(tasks):
        #    print(f"Task #{index+1}. {task}") #index+1 so lists start at 1 to be user firendly
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            status = " (Completed)" if index + 1 in CompletedTasks else ""
            print(f"Task #{index+1}. {task}{status}")
            
def deleteTask():
    listTasks()
    if not tasks:
        pass  #if empty just go back to original menu
    #do nothing unless list isnt empty
    else:
        try:
            taskToDelete = int(input("Enter the # to delete: "))
            taskToDelete-=1 #since we added one in the display the actual index is 1 less than that
           # if taskToDelete >= 0 and taskToDelete < len(tasks):
            if 0 <= taskToDelete < len(tasks):
                if taskToDelete + 1 in CompletedTasks:
                    CompletedTasks.remove(taskToDelete + 1)
                tasks.pop(taskToDelete)
                print(f"Task {taskToDelete+1} has been removed.")
                # Adjust the CompletedTasks set
                updatedCompletedTasks = set()
                for index in CompletedTasks:
                    if index > taskToDelete + 1:
                        updatedCompletedTasks.add(index - 1)  # Shift the index of tasks that come after the deleted task
                    else:
                        updatedCompletedTasks.add(index)
                CompletedTasks.clear()
                CompletedTasks.update(updatedCompletedTasks)
            else:
                print(f"Task #{taskToDelete+1} was not found.")
        except:
            print("Invalid input.")
        
def MarkComplete():
    listTasks() 
    incomplete_tasks = [i + 1 for i in range(len(tasks)) if i + 1 not in CompletedTasks]
    if incomplete_tasks:
       try:
         TaskIndex=int(input("Enter the # of the task you completed: "))
         #if TaskIndex>= 0 and TaskIndex <= len(tasks):
         if 1 <= TaskIndex <= len(tasks):
               CompletedTasks.add(TaskIndex)
               print(f"Task {TaskIndex} has been marked as completed.")
               #CompletedTasks[TaskIndex]=tasks[TaskIndex-1]
               #CompletedTasks.append(tasks[TaskIndex-1])
               #print(f"Task {TaskIndex} has been completed.")
               #tasks.remove(tasks[TaskIndex-1]) #remove completed task
         else:
               print(f"Task #{TaskIndex} was not found.")
       except:
           print("Invalid input.")    
    else:
       print("All tasks are complete!")
       return
       
        
    
    
def ViewComplete():
    if not CompletedTasks:
        print("There are no completed tasks.")
    else:
        print("Completed tasks:")
        for index in sorted(CompletedTasks):
            print(f"Task #{index}. {tasks[index-1]}")
        #for index, task in CompletedTasks.items():
           # print(f"Task #{index}. {task}")   
        #for j in range(len(CompletedTasks)):
        #    print(f"Task #{j+1}. {CompletedTasks[j]}")
    
def reminder():
    incomplete_tasks = [i + 1 for i in range(len(tasks)) if i + 1 not in CompletedTasks]
    if incomplete_tasks:
        print("These Tasks are not yet complete:")
        for i in incomplete_tasks:
            print(f"Task #{i}. {tasks[i-1]}")
    else:
        print("There are no tasks to do.")
    #for index, task in enumerate(tasks):
    #i=0
    #for task in tasks:
    #    if task not in CompletedTasks:
    #        print(f"Task #{i+1}. {task}")    
    #        i+=1
    
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
        #time.sleep(10)
        #reminder()
       
    print("Goodbye 👋👋")        
        
        #can add time function to remind user of tasks left
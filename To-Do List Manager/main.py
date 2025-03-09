print("Welcome to your To-Do List Manager! \n 1. View Tasks \n 2. Add Task \n 3. Mark Task as Completed \n 4. Delete Task \n 5. Exit")
inp = int(input("Select an option: "))
tasks = []


while(inp != 5):
    
    
    if(inp == 1):
        for ind,val in enumerate(tasks):
            print(ind+1,val["Task"],"[",val['Status'], "]")
        inp = int(input("Select an option: "))
        
    elif(inp == 2):
        tasks_dic = {}
        tasks_dic["Task"] = input("Add Task: ")
        tasks_dic["Status"] = "Not Completed"
        tasks.append(tasks_dic)
        inp = int(input("Select an option: "))
        
    elif(inp == 3):
        print("option 3: Enter the Number of Task To Mark Task As Completed")
        task_number = int(input("Enter the Number"))
        tasks[task_number-1]["Status"] = "Completed"
        inp = int(input("Select an option: "))
        
    elif(inp == 4):
        print("option 4: Enter the Number of Task to Delete it")
        task_number = int(input("Enter the Number"))
        del tasks[task_number-1]
        inp = int(input("Select an option: "))
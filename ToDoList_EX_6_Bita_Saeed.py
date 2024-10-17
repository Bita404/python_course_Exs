task_name =[]
task_status=[]
task_duration =[]

for i in range(200):
     answer = input("Add, Display, Remove, Edit, Search, Mark, Details, Help, Exit :")
     answer = answer.lower() 
     if answer == "add" :
         name = input("Task name :").lower()
         if name not in task_name :
            task_name.append(name)
            task_status.append(False)
            task_duration.append(None)
            print("Task Added Succesfully !") 
         else :
            print("This Task Already Exists !")
            
     elif answer == "display" :
         for i, name in enumerate(task_name) :
           print(i+1 , name , task_status[i], task_duration[i])
            
     elif answer == "remove" :
         name = input("Name For Remove: ").lower()
         if name in task_name :
             i  = task_name.index(name)
             task_name.pop(i)
             task_status.pop(i)
             task_duration.pop(i)
             print(f"{name} Task Removed succesfully !")
         else :
             print(f"'{name}' Not Found !")    
             
     elif answer == "edit" :
         name = input("Enter the task name for edit :").lower()
         if name in task_name :
             new_name = input("Enter the new name:").lower()
             if new_name not in task_name :
                 i = task_name.index(name)
                 task_name[i] = new_name
                 print(f"Task Edited to {new_name} Succesfully !")
             else :
                 print("This Task Already Exists !")  
         else :
             print("Task Not Found !")          
     elif answer == "search" :
         name =input ("Enter Task name :").lower()
         if name in task_name :
             i = task_name.index(name)
             print("Task:", task_name[i]," Status:",task_status[i] ," Duratiuon:",task_duration[i])
         else :
             print(f"'{name}' Task Not Found ! ")    
            
     elif answer == "mark" :
         name = input("Task name : ").lower()
         if name in task_name :
             i = task_name.index(name)
             start =float(input("Enter The Start Time Hour : "))
             end = float(input("Enter The End Time Hour: "))
             if 1<=start<=24 and 1<=end<=24:  # only hours , it doesnt contain minuets because it may need function (def)
                 if end > start :
                     task_duration[i] = end - start
                 elif start > end :
                     task_duration[i] = end + (24 - start) 
                 else :
                     task_duration[i] = 0  
                 task_status[i] = True
                 print("Task Marked as done : ")
                 print(f"Task name:{task_name[i]}  Task status:{task_status[i]}  Task duration:{task_duration[i]}hours ")
             else :
                 print("Invalid Time !")    
         else :
             print(f"'{name}' Task Not Found !")   
             
     elif answer == "details" :
         num_of_task = len(task_name)
         hours_worked =[]
         for h in task_duration :
             if h :
                 hours_worked.append(h)
                 sum_hours = sum(hours_worked)
                 
         done_task = task_status.count(True)
         not_done_task = task_status.count(False)
         print(f"Number Of Tasks : {num_of_task}")
         print(f"Hours Worked : {sum_hours}")
         print(f"Number Of Completed Tasks : {done_task}")
         print(f"Number Of Uncompleted Tasks : {not_done_task}")
         
     elif answer == "help" :
         print("Add: adding a new task")
         print("Display : showing all datas information")
         print("Remove : for removing a task from the list")
         print("Edit : to edit a takes name")
         print("Search : Look for an existing task")
         print("mark : mark a task as done")
         print("Details : shows all the details of tasks")
         print("Exit : ends the program")
     elif answer == "exit":
         break
     elif answer == "":
         continue
     else :
         print(f"{answer} Command Not Found ! ")
     
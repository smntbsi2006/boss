print("hello boss!\nhow can i help you?".title())
employee_list=[]
project_list=[]
done_list=[]
doing_list=[]
while True:
    request_boss=int(input("if you want to:\n1- join a employee press==> (1)"
    "\n2-creat new project press==> (2)\n3-add a project to done projects press==> (3)\n"
    "4-show all of the projects(doing and done) press==> (4)\n5-take a project to employee press==>(5)\n"
    "and if you want to exit press==> 0\n".title()))
    while request_boss in [1,2,3,4,5]:
    
        
        if request_boss==1:
            while input("do you want to join employee?".title()).lower() in ["yes","y"]:
                information={'name':"","phone_number":""}
                information["name"]=(input("enter employee-name:".title()))
                information["phone_number"]=input("enter employee-phone number:".title())

                employee_list.append(information)
        #print(employee_list)
            else:
                print("your data was saved".title())
                break
        if request_boss==2:
            while input("do you want to add project?".title()).lower() in ["yes","y"]:
                project={"name":"","duration":"","work":""}
                project["name"]=(input("enter name-project:".title()))
                project["duration"]=input("enter duration need for project:".title())
                project["work"]=input("enter project-work: ".title())
                project_list.append(project)

            else:
                print("your data was saved".title())
                break
        if request_boss==3:
            while input("do you want to add project to done-project?".title()).lower() in ["yes","y"]:  
                done_project=input("enter the project-name you have to done:")
                time=int(input("how much time he/she used?"))

                for project in doing_list:
                    
                    if project["name"]==done_project:
                        project["time"]=time

                        done_list.append(project)
                        doing_list.remove(project)
                        project
                        print("project moved!")
                        break
            else:
                print("your data was saved".title())
                break
        if request_boss==4:
            print(f"doing-list:{doing_list}\ndone-list:{done_list}")
            break
        if request_boss==5:
            found=False
            while input("do you want to take a project to employee?".title()).lower() in ["yes","y"]:
                project_name=input("enter project-name you want: ")
                employee_phone=input("enter employee-phone number you want:")
                for employee in employee_list:
                    if employee["phone_number"]==employee_phone:
                        found=True
                        

                        for projec in project_list:
                            if projec["name"]==project_name:
                                projec["employee_name"]=employee["name"]
                                projec["employee_phone"]=employee["phone_number"]

                                doing_list.append(projec)
                                project_list.remove(projec)
                                print("project moved.")
                                break
                if not found:
                    print("employee not found!\ntry again")
            else:
                print("your data was saved".title())
                break         

    if request_boss==0:
        print("see you boss!".title())
        break




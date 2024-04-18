#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime # import datetime to get current time
import pwinput as pwinput # import pwinput to hide password input
# you need to create your own user.txt and task.txt files before runing the porgram
#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''
# Open user file to retrive usernames and passwords
with open('user.txt', 'r') as file: # open file as read only 
    user_data = file.read().splitlines() # this call each line and store it in a list i.e. ["admin,ad1min","username,password"]
# Itterate on each value in the list to retrive username and password and store it in dictionary
users = {}
for user in user_data:
    username, password = user.split(', ')
    users[username] = password
logged_in = False

# Check if Loging status if not logged ask you to login and the loop will breal when logged
while logged_in != True:
    username = input("Enter your username: ")
    password = pwinput.pwinput( prompt="Enter your password: ")
    if username in users and users[username] == password:
        logged_in = True
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")
# Start the program loop
while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.

    # The admin menue shows only admin is logged 
    if username == 'admin':
         menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - statistics 
e - exit
: ''').lower()
    # other user's menu
    else: 
        menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
    # registration function. can only be accessed by admin.   
    if menu == 'r' and username == "admin":
        
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        
        new_username = input("Enter new username: ")
        new_password = pwinput.pwinput(prompt="Enter new password: ")
        confirm_password = pwinput.pwinput(prompt="Confirm the password: ")
        
        # Confirm password before storing
        if new_password == confirm_password:
            users[new_username] = new_password
            with open('user.txt', 'a') as file: # 'a' viwe as read and write but dosent change past values 
                file.write(f'\n{new_username}, {new_password}')
            print("User registered successfully!")
        
        # If the passoword dosent match 
        else:
            print("Passwords do not match. Registration failed.")

    # Add task menu 
    elif menu == 'a':
        
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''
        
        current_date = datetime.datetime.now().strftime("%Y-%m-%d") # Calling datetime to get current date
        username_task = input("Enter the username of the person assigned to the task: ")
        title_task = input("Enter the title of the task: ")
        task_description = input("Enter the description: ")
        due_date = input("Enter the due date [YYYY-MM-DD]: ")
       
       # Here store the task title and assigned date and username and due date in the diseried format 
        with open('tasks.txt', 'a') as file: 
            file.write(f'\n{username_task}, {title_task}, {task_description}, {current_date}, {due_date}, No')
        print("Task added successfully!")
    # View all menu 
    elif menu == 'va':
        
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''
        
        print("All tasks:")

        # Read tasks file 
        with open('tasks.txt', 'r') as file:
            tasks = file.read().splitlines() # store each line in a list

            # ittrate in each line 
            for task in tasks:
                task_data = task.split(', ') # here comma used as split point, where it will be stored in arry
                # now calling fungition depending on the task file format 
                print(f'Task: {task_data[1]}')
                print(f'Assigned to: {task_data[0]}')
                print(f'Date assigned: {task_data[3]}')
                print(f'Due date: {task_data[4]}')
                print(f'Task complete? {task_data[5]}')
                print(f'Task description: {task_data[2]}')
                print("")
    # view current user task 
    elif menu == 'vm':
        
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        
        print(f'Tasks assigned to {username}:')
        with open('tasks.txt', 'r') as file:
            tasks = file.read().splitlines()
            for task in tasks:
                task_data = task.split(', ')

                # Get signed username task only
                if task_data[0] == username:
                    print(f'Task: {task_data[1]}')
                    print(f'Date assigned: {task_data[3]}')
                    print(f'Due date: {task_data[4]}')
                    print(f'Task completion status: {task_data[5]}')
                    print(f'Task description: {task_data[2]}')
                    print("")
    # statistics menu. can be only accessed by the admin
    elif menu == 's' and username == "admin":
        total_users = len(users) # get toalt number of users 
        total_tasks = 0

        with open('tasks.txt', 'r') as file:
            tasks = file.read().splitlines() # split each line as it contain one task 
            total_tasks = len(tasks) # get total number of  task 
        # Display Statistics
        print("_________ Statistics _________")
        print(f"Total number of users: {total_users}")
        print(total_users*"=")
        print(f"\nTotal number of tasks: {total_tasks}")
        print(total_tasks*"=")
        print("______________________________")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")
# Initialize an empty dictionary to store users
user_database = {}
user_profiles = {}
user_tasks = {}

# Function to register a user
def register_user():
    print("\n--- Register ---")
    username = input("Enter a username: ")
    if username in user_database:
        print("Username already exists! Try again.")
        return
    password = input("Enter a password: ")
    if len(password) < 6:
        print("Password must be at least 6 characters long!")
        return
    user_database[username] = password
    user_profiles[username] = {"Name": "", "Address": "", "Phone": "", "DOB": ""}
    user_tasks[username] = []
    print("Registration successful!")

# Function to log in a user
def login_user():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    if username not in user_database:
        print("Username not found! Please register first.")
        return
    password = input("Enter your password: ")
    if user_database[username] == password:
        print(f"\nWelcome back, {username}!")
        user_dashboard(username)
    else:
        print("Incorrect password! Try again.")

# Dashboard after successful login
def user_dashboard(username):
    while True:
        print(f"\n--- Dashboard: {username} ---")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Manage Tasks")
        print("4. Change Password")
        print("5. Logout")
        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
        if choice == "1":
            view_profile(username)
        elif choice == "2":
            update_profile(username)
        elif choice == "3":
            manage_tasks(username)
        elif choice == "4":
            change_password(username)
        elif choice == "5":
            print(f"Goodbye, {username}!")
            break
        else:
            print("Invalid choice! Please try again.")

# View Profile
def view_profile(username):
    print(f"\n--- Profile ---")
    profile = user_profiles[username]
    print(f"Name: {profile['Name']}")
    print(f"Address: {profile['Address']}")
    print(f"Phone: {profile['Phone']}")
    print(f"Date of Birth: {profile['DOB']}")

# Update Profile
def update_profile(username):
    print(f"\n--- Update Profile ---")
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    user_profiles[username].update({"Name": name, "Address": address, "Phone": phone, "DOB": dob})
    print("Profile updated successfully!")

# Manage Tasks
def manage_tasks(username):
    while True:
        print(f"\n--- Task Manager: {username} ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Back to Dashboard")
        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
        if choice == "1":
            add_task(username)
        elif choice == "2":
            view_tasks(username)
        elif choice == "3":
            update_task(username)
        elif choice == "4":
            delete_task(username)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

# Add Task
def add_task(username):
    task = input("Enter the task description: ")
    user_tasks[username].append(task)
    print("Task added successfully!")

# View Tasks
def view_tasks(username):
    print(f"\n--- Tasks for {username} ---")
    tasks = user_tasks[username]
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Update Task
def update_task(username):
    view_tasks(username)
    tasks = user_tasks[username]
    if not tasks:
        return
    task_num = int(input("Enter the task number to update: "))
    if 1 <= task_num <= len(tasks):
        new_task = input("Enter the new task description: ")
        tasks[task_num - 1] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task number!")

# Delete Task
def delete_task(username):
    view_tasks(username)
    tasks = user_tasks[username]
    if not tasks:
        return
    task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1)
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")

# Change Password
def change_password(username):
    print("\n--- Change Password ---")
    old_password = input("Enter your current password: ")
    if user_database[username] != old_password:
        print("Incorrect current password! Password not changed.")
        return
    new_password = input("Enter a new password: ")
    if len(new_password) < 6:
        print("Password must be at least 6 characters long!")
        return
    user_database[username] = new_password
    print("Password updated successfully!")

# Run the main program loop
while True:
    print("\n--- User Dashboard Management System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")

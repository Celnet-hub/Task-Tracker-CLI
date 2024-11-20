import json
from datetime import datetime

greetings = '''
Hi, Welcome to your Tasks Tracker where you manage your tasks.

You can perform the following actions:
1 - Add task
2 - Update task
3 - Delete tasks
4 - List tasks

Enter the number representation of the actions you want to perform:
'''

# create a Tasks Class and define properties
class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()
        self.next_id = max(self.tasks.keys(), default=0) + 1

    # get existing tasks and return 
    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                contents = file.read()
                if contents:
                    previous_tasks = json.loads(contents)
                    return {task["id"]: task for task in previous_tasks}
                else:
                    return {}
        except FileNotFoundError:
            return {}

    def create_task(self, description):
        task = {
            "id": self.next_id,
            "description": description,
            "status": None,
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat()
        }
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task
    
    # update tasks status
    def update_task_status(self, task_id, new_status):
        task = self.tasks.get(task_id)
        if task:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            print(json.dumps(task, indent=4))
            self.tasks[task_id] = task
            self.save_tasks()
        else:
            print(f'Task with ID {task_id} does not exist in the database')

    # update tasks description
    def update_task_description(self, task_id, new_description):
        task = self.tasks.get(task_id)
        if task:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            print(json.dumps(task, indent=4))
            self.tasks[task_id] = task
            self.save_tasks()
        else:
            print(f'Task with ID {task_id} does not exist in the database')
    
    # update tasks description
    def delete_task(self, task_id):
        tasks = self.load_tasks()
        task = self.tasks.get(task_id)
        if task_id in tasks:
            print(True)
            confirmation = input(f'Delete Task: {task}? Y/N: ')
            if confirmation.lower() == 'y' or confirmation.lower() == 'yes': 
                tasks.pop(task_id)
                print(f'Task with ID {task_id} has been deleted')
                print(json.dumps(tasks, indent=4))
                self.tasks = tasks
                self.save_tasks()

                       
    # save to list
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(list(self.tasks.values()), file, indent=4)

# create a function that gets user input
def get_user_input(greetings):
    attempts = 0
    print(greetings)
    while attempts < 3:
        user_input = input("Please enter action number: ")
        try:
            user_input = int(user_input)
            if user_input in range(1, 5):
                return user_input
            else:
                attempts += 1
                print('Invalid action number, try again!!', 3 - attempts, "attempts left")
        except ValueError:
            attempts += 1
            print('Please input a number.', 3 - attempts, "attempts left")



#initialize TaskManager class
task_manager = TaskManager('tasks.json')

# get user input
user_input = get_user_input(greetings)

# Add tasks
if user_input == 1: 
    task = input("Enter Task: ")
    outcome = task_manager.create_task(task)
    task_manager.save_tasks()
    print("Task added successfully")

# Update Task
elif user_input == 2:
    task_id = int(input("Proivde Task ID: "))
    next_update = int(input("Input 1 for Status_Update or Input 2 for Task_Description update: "))
    if next_update == 1:
        new_status = input('Enter new status (HINT: Todo, Done, In Progress): ')
        task_manager.update_task_status(task_id, new_status)
    elif next_update == 2:
        new_description = input('Enter new tasks description: ')
        task_manager.update_task_description(task_id,new_description)


# Delete Task
elif user_input == 3:
    task_id = int(input("Proivde Task ID: "))
    task_manager.delete_task(task_id)

# List Tasks
elif user_input == 4:
    tasks = task_manager.load_tasks()
    if tasks == {}:
        print("You do not have any tasks\n", tasks)
    else:
        pretty_tasks = json.dumps(task_manager.load_tasks(), indent=4)
        print("These are your tasks: \n", pretty_tasks)


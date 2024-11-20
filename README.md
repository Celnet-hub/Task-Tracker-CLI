# Task Tracker

Welcome to your [Task Tracker!](https://github.com/Celnet-hub/Task-Tracker-CLI). This application allows you to manage your tasks efficiently.

## Features

- **Add Task**: Create a new task with a description.
- **Update Task**: Update the status or description of an existing task.
- **Delete Task**: Remove a task from the task list.
- **List Tasks**: Display all tasks in a readable format.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Celnet-hub/Task-Tracker-CLI.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Task-Tracker-CLI
    ```
3. Ensure you have Python installed. This project requires Python 3.6 or higher.

## Usage

1. Run the application:
    ```sh
    python task_tracker.py
    ```

2. Follow the on-screen instructions to perform the desired actions.

## Code Overview

The core functionality is handled by the `TaskManager` class and user interaction is managed through a simple console-based interface.

### TaskManager Class

- **Initialization**:
    ```python
    class TaskManager:
        def __init__(self, filename):
            self.filename = filename
            self.tasks = self.load_tasks()
            self.next_id = max(self.tasks.keys(), default=0) + 1
    ```

- **Loading Tasks**:
    ```python
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
    ```

- **Creating a Task**:
    ```python
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
    ```

- **Updating Task Status**:
    ```python
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
    ```

- **Updating Task Description**:
    ```python
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
    ```

- **Deleting a Task**:
    ```python
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
    ```

- **Saving Tasks**:
    ```python
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(list(self.tasks.values()), file, indent=4)
    ```

### User Interaction

- **Getting User Input**:
    ```python
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
    ```

### Example Usage

- **Initializing TaskManager**:
    ```python
    task_manager = TaskManager('tasks.json')
    ```

- **Adding Tasks**:
    ```python
    if user_input == 1: 
        task = input("Enter Task: ")
        outcome = task_manager.create_task(task)
        task_manager.save_tasks()
        print("Task added successfully")
    ```

- **Updating Tasks**:
    ```python
    elif user_input == 2:
        try:
            task_id = int(input("Proivde Task ID: "))
            next_update = int(input("Input 1 for Status_Update or Input 2 for Task_Description update: "))
            if next_update == 1:
                new_status = input('Enter new status (HINT: Todo, Done, In Progress): ')
                task_manager.update_task_status(task_id, new_status)
            elif next_update == 2:
                new_description = input('Enter new tasks description: ')
                task_manager.update_task_description(task_id,new_description)
        except ValueError as e:
            print('Please input a number')
    ```

- **Deleting Tasks**:
    ```python
    elif user_input == 3:
        try:
            task_id = int(input("Proivde Task ID: "))
            task_manager.delete_task(task_id)
        except ValueError as e:
            print('Please input a number')
    ```

- **Listing Tasks**:
    ```python
    elif user_input == 4:
        tasks = task_manager.load_tasks()
        if tasks == {}:
            print("You do not have any tasks\n", tasks)
        else:
            pretty_tasks = json.dumps(task_manager.load_tasks(), indent=4)
            print("These are your tasks: \n", pretty_tasks)
    ```

### Sample `tasks.json` File

Here is an example of how the data in the `tasks.json` file might

```json
[
    {
        "id": 1,
        "description": "Finish Tasks tracker project",
        "status": "Done",
        "createdAt": "2024-11-20T20:17:17.990778",
        "updatedAt": "2024-11-20T20:50:33.366086"
    },
    {
        "id": 3,
        "description": "Implement error handling",
        "status": "In Progress",
        "createdAt": "2024-11-20T20:17:46.461264",
        "updatedAt": "2024-11-20T20:55:41.252964"
    }
]

```

## Conclusion

This project provides a simple yet effective way to manage tasks from the command line. Feel free to modify and expand it according to your needs.

## License

This project is licensed under the MIT License.

---

Enjoy managing your tasks with ease!

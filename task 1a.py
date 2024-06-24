class TaskManager:
    def init(self):
        self.tasks = {}

    def add_task(self, task_name, task_time):
        if task_time in self.tasks:
            self.tasks[task_time].append(task_name)
        else:
            self.tasks[task_time] = [task_name]
        return f"Task '{task_name}' scheduled at {task_time}."

    def get_tasks(self, task_time):
        if task_time in self.tasks:
            return self.tasks[task_time]
        else:
            return []

    def remove_task(self, task_name, task_time):
        if task_time in self.tasks and task_name in self.tasks[task_time]:
            self.tasks[task_time].remove(task_name)
            if len(self.tasks[task_time]) == 0:
                del self.tasks[task_time]
            return f"Task '{task_name}' at {task_time} removed."
        else:
            return f"Task '{task_name}' at {task_time} not found."

    def list_all_tasks(self):
        if not self.tasks:
            return "No tasks scheduled."
        else:
            task_list = ""
            for task_time, tasks in self.tasks.items():
                task_list += f"At {task_time}: {', '.join(tasks)}\n"
            return task_list.strip()


task_manager = TaskManager()

def main():
    print("Welcome to Task Manager Bot!")
    print("How can I assist you today?")

    while True:
        user_input = input("Enter your command (add/remove/get/list/exit): ").strip().lower()

        if user_input == 'add':
            task_name = input("Enter task name: ").strip()
            task_time = input("Enter task time (e.g., '9 AM', '2 PM'): ").strip().lower()
            print(task_manager.add_task(task_name, task_time))

        elif user_input == 'remove':
            task_name = input("Enter task name: ").strip()
            task_time = input("Enter task time (e.g., '9 AM', '2 PM'): ").strip().lower()
            print(task_manager.remove_task(task_name, task_time))

        elif user_input == 'get':
            task_time = input("Enter time to get tasks for (e.g., '9 AM', '2 PM'): ").strip().lower()
            tasks = task_manager.get_tasks(task_time)
            if tasks:
                print(f"Tasks at {task_time}: {', '.join(tasks)}")
            else:
                print(f"No tasks scheduled at {task_time}.")

        elif user_input == 'list':
            print(task_manager.list_all_tasks())

        elif user_input == 'exit':
            print("Exiting Task Manager Bot. Have a great day!")
            break

        else:
            print("Invalid command. Please try again.")


if name == "main":
    main()

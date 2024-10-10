from Task import *

class Manager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, title, description, task_id):
        if not task_id.isnumeric():
            raise ValueError("Task ID must be numeric.")
        if task_id in self.tasks:
            raise ValueError(f"Task ID {task_id} already exists.")
        task = Task(title, description, task_id)
        self.tasks[task_id] = task

    def mark_task_done(self, task_id):
        if task_id not in self.tasks:
            raise ValueError(f"No task found with ID {task_id}")
        self.tasks[task_id].mark_done()

    def display_tasks(self):
        if not self.tasks:
            return "No tasks available."
        return "\n".join([task.display_task() for task in self.tasks.values()])

    def task_summary(self):
        completed_count = 0
        not_completed_count = 0
    
        for task in self.tasks.values():
          if task.status:
              completed_count += 1
          else:
             not_completed_count += 1
    
        return (f"Completed Tasks: {completed_count}\n"
            f"Pending Tasks: {not_completed_count}")


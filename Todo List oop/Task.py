from datetime import datetime

class Task:
    def __init__(self, title, description, task_id):
        self.title = title
        self.description = description
        self.task_id = task_id
        self.start_time = datetime.now()
        self.end_time = None
        self.status = False

    def mark_done(self):
        self.status = True
        self.end_time = datetime.now()

    def display_task(self):
        status = 'Done' if self.status else 'Not Done'
        end_time_str = self.end_time.strftime("%Y-%m-%d %H:%M:%S") if self.end_time else "N/A"
        return (f"Task ID: {self.task_id}\n"
                f"Title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Start Time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"End Time: {end_time_str}\n"
                f"Status: {status}\n")

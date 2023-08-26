import threading
import time
from logger import BaseAppLogger


class Scheduler(BaseAppLogger):
    def __init__(self):
        self.scheduled_tasks = []
        self.worker_thread = threading.Thread(target=self.run_scheduled_tasks)
        self.worker_thread.daemon = True
        self.worker_thread.start()

    def schedule_task(self, task_callable, interval_seconds=21600):
        if callable(task_callable):
            self.log(
                f"Scheduling task {task_callable} at an interval {interval_seconds}"
            )
            self.scheduled_tasks.append((task_callable, interval_seconds))
        else:
            self.log(f"Unable to schedule task: {task_callable}. Not a callable")

    def run_scheduled_tasks(self):
        while True:
            for task_callable, interval_seconds in self.scheduled_tasks:
                try:
                    task_callable()
                except Exception as e:
                    self.log(f"Error in scheduled task: {e}", "debug")
                time.sleep(interval_seconds)


scheduler = Scheduler()

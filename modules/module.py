from datetime import datetime


class Module():

    recurring_in_seconds = NotImplementedError
    action = NotImplementedError

    def __init__(self):
        self.last_run = datetime.min

    def run(self):
        self.action()
        self.last_run = datetime.now()

    def should_run(self):
        since_last_run = datetime.now() - self.last_run
        return since_last_run.total_seconds() > self.recurring_in_seconds

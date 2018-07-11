import random

# The Task class will represent a single printing task.

class Task:

    def __init__(self, time):
        self.timestamp = time # Time that tells when the task got pushed into the Queue.
        self.pages = random.randrange(1, 20) # The task will have 1 - 20 page task.

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    # Calculate how long it waited to get processed
    def wait_time(self, current_time):
        return current_time - self.timestamp

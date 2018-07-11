class Printer:

    def __init__(self, ppm):
        self.page_rate = ppm # How many pages it will print per minute
        self.current_task = None #
        self.time_remaining = 0 # Remaining time

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate



# pages -> 5
# page_rate -> 5
# * 60

# pages * 60 / page_rate
# 5 pages * 60 sec / 5 pages per min = takes 60 second (1 min for 5 pages)
# 20 pages * 60 sec / 5 pages per min = takes 240 second (4 min for 20 pages)
#

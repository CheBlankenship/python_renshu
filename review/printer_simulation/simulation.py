from task import Task
from printer import Printer
from printer_queue import PrintQueue
import random



def simulation(total_time, pages_per_min):

    lab_printer = Printer(pages_per_min) # set printer per min
    print_q = PrintQueue() # set the queue
    waiting_time = [] #

    for current_second in range(total_time):

        if new_print_task():
            t = Task(current_second)
            print_q.enqueue(t)

        if (not lab_printer.busy()) and (not print_q.is_empty()):
            next_task = print_q.dequeue()
            waiting_time.append(t.wait_time(current_second))
            lab_printer.start_next(next_task)

        # If any of the statement doesn't match, process the current_task which
        # is in the printer and sub the time it is taking.
        lab_printer.tick()

    avg_wait = sum(waiting_time)  / len(waiting_time)
    print("Average Wait %6.2f secs %3d tasks remaining." %(avg_wait, print_q.size()))




def new_print_task():
    rand_num = random.randrange(1, 181)
    if rand_num == 180:
        return True
    else:
        False



for i in range(10):
   simulation(3600, 5)

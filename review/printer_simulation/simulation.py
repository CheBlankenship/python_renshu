from task import Task
from printer import Printer
from printer_queue import PrintQueue
import random



def simulation(total_time, pages_per_min, num_of_students):

    lab_printer = Printer(pages_per_min) # set printer per min
    print_q = PrintQueue() # set the queue
    waiting_time = [] #


    for current_second in range(total_time):

        # create new print task and put it into the queue.
        if new_print_task(num_of_students):
            # print("CREATE NEW TASK")
            t = Task(current_second)
            print_q.enqueue(t)

        # if the printer is not busy and if the queue is not empty,
        # process the next waiting print task
        # check how long the task was waiting in the queue and add it to the array.
        # when the start_next() gets called, it will check how many seconds it will take to complete.
        # it will set it to busy() = True and current_task = next_task.
        # When the printer time_remaining gets 0, it will change busy() = False.
        if (not lab_printer.busy()) and (not print_q.is_empty()):
            # print("PROCESSSING CURRENT TASK")
            next_task = print_q.dequeue()
            waiting_time.append(t.wait_time(current_second))
            lab_printer.start_next(next_task)

        # If any of the statement doesn't match, process the current_task which
        # is in the printer and sub the time it is taking.
        lab_printer.tick()


    avg_wait = sum(waiting_time)  / len(waiting_time)
    print("Average Wait %6.2f secs %3d tasks remaining." %(avg_wait, print_q.size()))


# Range 1 - 181#
# Number students : 10
# Pages per task : 1 - 20
# If there are 10 students and each prints twice, then there are 20 print tasks per hour.
# 40/1 -> 20/



def new_print_task(num_of_students):
    # print("Range >> ", int((60*60)/(num_of_students*2)+1))

    rand_num = random.randrange(1, int((60*60)/(num_of_students*2)+1))
    if rand_num == int((60*60)/(num_of_students*2)):
        return True
    else:
        False


# new_print_task(20)

for i in range(10):
   simulation(3600, 15, 11)

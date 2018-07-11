class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_emqty(self):
        return [] == self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



def hot_postato(name_list, num):

    sim_queue = Queue()

    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()

    return sim_queue.dequeue()



print(hot_postato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))

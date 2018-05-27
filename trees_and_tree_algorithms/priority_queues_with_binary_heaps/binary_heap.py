class BinaryHeap:

    def __init__(self):
        self.heap_list  = [0]
        self.current_size = 0

    def __repr__(self):
        return str(self.heap_list)

    def __str__(self):
        return str(self.heap_list)

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp

            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.percolate_up(self.current_size)

    def percolate_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.percolate_down(1)
        return ret_val

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while (i > 0):
            self.percolate_down(i)
            i = i - 1



bh = BinaryHeap()
bh.build_heap([5, 9, 11, 14, 18, 19, 21, 33, 17, 27])
# 0
# 5 - 11
#        - 19
#        - 21
#   - 9
#        - 14
#             - 33
#             - 17
#        - 18
#             - 27

bh.insert(7)
# Integer 7 will be in the level 4 second branch right.[11]
# The parent node for 7 is 18 which index is [5].
# Swap 7 and 18
# The parent node for 7 changes to 9 which index is [2].
# Swap 7 and 9
# Parent node for 7 changes to 5
# 5 is smaller than 7 so it will remain the way it is.

print(bh)

# Best case hashing : O(1)
#

class HashTable:

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash_v, size):
        return (old_hash_v + 1) % size

    def put(self, key, data):
        hash_v = self.hash_function(key, len(self.slots))

        # If the slots[index] is None, link slots[index]=key and slots[index]=data
        if self.slots[hash_v] == None:
            self.slots[hash_v] = key
            self.data[hash_v] = data
        else:
            if self.slots[hash_v] == key:
                self.data[hash_v] = data
            else:
                next_slot = self.rehash(hash_v, len(self.slots))
                while (self.slots[next_slot] != None) and (self.slots[next_slot] != key):
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    # Replace data
                    self.data[next_slot] = data

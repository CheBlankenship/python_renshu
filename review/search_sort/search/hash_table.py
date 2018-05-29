# Best case hashing : O(1)
#



class HashTable:

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __repr__(self):
        return str(self.slots) + "\n" + str(self.data)

    def hash_function(self, key, size):
        # size が　11 の為、0 - 11 の範囲で余りが出る (index = [0] ~ [11])。
        # よって IndexError を起こすことを防ぐことができる。
        return key % size

    def rehash(self, old_hash_v, size):
        return (old_hash_v + 1) % size

    def put(self, key, data):
        hash_v = self.hash_function(key, len(self.slots))

        # If the slots[index] is None, link slots[index]=key and slots[index]=data
        if self.slots[hash_v] == None:
            print("hey")
            self.slots[hash_v] = key
            self.data[hash_v] = data
        else:
            # もしslots[index]のポジションが既に同じ値のkeyを所持していた場合、data[index]を上書きする。
            # 例：slots[0] = 44 (44 % 11 = 4 ... 0)
            if self.slots[hash_v] == key:
                print("OVER WRITE >> ", key)
                self.data[hash_v] = data
            #もしslots[index]
            # 例：slots[0] = 44となっている為、key=77は次の空いているポジションに移動をする。
            # 77 % 11 = 7 ... 0 and 44 % 11 = 4 ... 0
            # slots[0] = 44
            # slots[1] = 77
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







arr = [None] * 11
# [None, None, None, None, None, None, None, None, None, None, None]
arr[5] = "insert 1"
arr[6] = "insert 2"
# [None, None, None, None, None, 'insert 1', 'insert 2', None, None, None, None]
arr[6] = "insert 3"


h = HashTable()
h.put(5, "insert 1")
h.put(6, "insert 2")
# [None, None, None, None, None, 'insert 1', 'insert 2', None, None, None, None]
h.put(6, "insert 3")
# h[6] = "insert 3"
print(h)

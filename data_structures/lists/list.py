class List:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def add(self, item):
        self.items.append(item)
        return None

    def search(self, item):
        if item in self.items:
            return True
        else:
            return False

    def is_empty(self):
        return [] == self.items

    def remove(self, item):
        not_found = True
        position = 0
        while not_found and len(self.items)-1 >= position:
            if self.items[position] == item:
                not_found = False
                self.items.pop(position)
                print("hit")
                return None
            else:
                position = position + 1
                not_found = True

        if not_found == True:
            print("go")
            return "No item to remove."


    def size(self):
        return len(self.items)

    def append(self, item):
        if not item in self.items:
            self.items.append(item)
            return None
        else:
            return None

    def index(self, item):
        not_found = True
        position = 0
        print("Len >> ", len(self.items))
        while not_found and len(self.items)-1 >= position:
            print("compare >> ", self.items[position], " ", item)
            if self.items[position] == item:
                print("hit")
                not_found = False
                return position
            else:
                position = position + 1
                not_found = True

        if not_found == True:
            return "No item found."

    def insert(self, pos, item):
        self.items.insert(pos, item)
        return None

    # def pop(self):
    #     return self.items.pop()
    #
    # def pop(self, pos):
    #     return self.items.pop(pos)






l = List()
l.add("a")
l.add("b")
l.add("c")
l.size()
# l.append("c")
print(l.remove("c"))
print(l.index("c"))
print(l.pop())

print("Result >>> ", l)

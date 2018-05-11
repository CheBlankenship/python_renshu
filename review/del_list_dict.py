import time





def deleteDict():
    dict = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6
    }

    start = time.time()
    del dict["2"]
    end = (time.time() - start) * 100000
    print("Time dict >> ", end)


def deleteList():
    list = [1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,61,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5]
    start = time.time()
    del list[1]
    end = (time.time() - start) * 100000
    print("time list >> ", end)



print(deleteList())
print(deleteDict())

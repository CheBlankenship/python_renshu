# Example one

def list_sum_one(num_list):
    sum = 0
    for number in num_list:
        sum = sum + number

    return sum




# Example two
def list_sum_two(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum_two(num_list[1:])




print(list_sum_two([1,2,3,4]))

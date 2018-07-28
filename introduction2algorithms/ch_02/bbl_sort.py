
# Time complexity: (n^2/2) + (n/2) = O(n^2)

def bbl_sort(array):
    # Set it to arr-1 so it dosen't cause out range.
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            #swap if current_value > next_value = True
            if array[j] > array[j+1]:
                temp = array[i] # Space complexity : O(1)
                array[i] = array[i+1]
                array[i+1] = temp

    return array

print(bbl_sort([6,9,22,34,67]))

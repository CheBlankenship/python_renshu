


def insertionSort(array):

    for index in range(1, len(array)):

        current_value = array[index]
        position = index # Save the current position.

        # Loop while current_value is smaller than previouse value.
        # Stop when it hits the init index.
        while (position > 0) and (current_value < array[position - 1]):
            # If the conditions are True. Override the index[position].
            array[position - 1] = array[position] # shif element by element
            # change the position (move one more previouse).
            position = position - 1

        # When it hits the head of list or when current_value is larger., it will turn False.
        # Insert the current_value into the position.
        array[position] = current_value

    return array



print("Result: ", insertionSort([3,6,7,100,45,33,24]))

# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # Loop through arr starting at the current index
        for j in range(cur_index + 1, len(arr)):

            # compare j value with smallest index value
            if arr[j] < arr[smallest_index]:

                # if j is smaller than the current smallest index replace smallest index
                smallest_index = j

        # Swap current index and smallest index
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


def bubble_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):

        # loop through n-1-n elements
        for j in range(len(arr) - 1):

            # compare current value with next value
            if arr[j] > arr[j+1]:

                # if current value > next value, swap values
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


# Complex sorting algo

# 200

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
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

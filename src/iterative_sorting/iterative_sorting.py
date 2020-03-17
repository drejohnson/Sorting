# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # sets default min value
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # get elements to the right of current_index
        right_of_index = cur_index+1
        for j in range(right_of_index, len(arr)):
            # if list in j position is less than list at current min value replace min value
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # if item smaller the current index swap
        if smallest_index != cur_index:
            arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    sorted = False
    while not sorted:
        sorted = True

        for i in range(0, len(arr) -1):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
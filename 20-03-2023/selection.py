import random

ARR_LEN = 20

def selection_sort(arr):

    for i in range(len(arr)):

        min_index = i

        for j in range(i+1, len(arr)):

            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr    


if __name__ == "__main__":

    print("=====SELECTION SORT=====")

    arr = []
    print("Enter the array: ")
    arr = list(map(int, input().split()))
    arr = [ random.randrange(1, 100, 1 ) for i in range(0, ARR_LEN ) ]

    print(arr)

    print( selection_sort(arr) )
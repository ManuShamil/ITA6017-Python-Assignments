import random

ARR_LEN = 20

def bubble_sort( arr ):
        
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
        return arr


if __name__ == "__main__":

    print("=====BUBBLE SORT=====")

    arr = []
    print("Enter the array: ")
    arr = [ random.randrange(1, 100, 1 ) for i in range(0, ARR_LEN ) ]

    print(arr)

    print( bubble_sort(arr) )
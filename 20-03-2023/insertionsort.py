import random

ARR_LEN = 20

def insertion_sort( arr ):
    
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    
        return arr


if __name__ == "__main__":

    print("=====INSERTION SORT=====")

    arr = []
    print("Enter the array: ")
    arr = list(map(int, input().split()))
    arr = [ random.randrange(1, 100, 1 ) for i in range(0, ARR_LEN ) ]

    print(arr)

    print( insertion_sort(arr) )
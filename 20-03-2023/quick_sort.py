import random

ARR_LEN = 20

def quick_sort(arr):
    
        if len(arr) <= 1:
            return arr
    
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
    
        return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":

    print("=====QUICK SORT=====")

    arr = []
    print("Enter the array: ")
    arr = list(map(int, input().split()))
    arr = [ random.randrange(1, 100, 1 ) for i in range(0, ARR_LEN ) ]

    print(arr) 

    print( quick_sort(arr) )
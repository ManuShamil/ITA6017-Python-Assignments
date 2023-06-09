import random

ARR_LEN = 20

def merge_sort( arr ):
    
        if len(arr) > 1:
    
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
    
            merge_sort(left)
            merge_sort(right)
    
            i = j = k = 0
    
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
    
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
    
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
    
        return arr

if __name__ == "__main__":

    print("=====MERGE SORT=====")

    arr = []
    print("Enter the array: ")
    arr = list(map(int, input().split()))
    arr = [ random.randrange(1, 100, 1 ) for i in range(0, ARR_LEN ) ]

    print(arr)

    print( merge_sort(arr) )